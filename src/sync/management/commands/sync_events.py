from datetime import date, datetime, timedelta

import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from sync.models import Event, SyncLog

EVENTS_API_URL = "https://events.k3scluster.tech/api/events/"

class Command(BaseCommand):
    help = 'Sync events from events-provider service'

    def add_arguments(self, parser):
        parser.add_argument(
            '--date',
            help='Sync events changed on specific date (YYYY-MM-DD)'
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Sync all available events'
        )

    def handle(self, *args, **options):
        sync_log = SyncLog.objects.create(
            date_filter=options['date'],
            sync_all=options['all']
        )

        try:
            params = {}
            if not options['all']:
                if options['date']:
                    sync_date = datetime.strptime(options['date'], '%Y-%m-%d').date()
                else:
                    sync_date = (timezone.now() - timedelta(days=1)).date()
                params['changed_at'] = sync_date.strftime('%Y-%m-%d')
                sync_log.date_filter = sync_date

            self.stdout.write(f"Starting sync with params: {params}")
            response = requests.get(EVENTS_API_URL, params=params)
            response.raise_for_status()

            events_data = response.json()
            new_count = 0
            updated_count = 0

            for event_data in events_data:
                defaults = {
                    'name': event_data['name'],
                    'date': event_data['date'],
                    'place': event_data['place'],
                    'changed_at': event_data['changed_at']
                }
                obj, created = Event.objects.update_or_create(
                    external_id=event_data['id'],
                    defaults=defaults
                )
                if created:
                    new_count += 1
                else:
                    updated_count += 1

            sync_log.new_events = new_count
            sync_log.updated_events = updated_count
            sync_log.status = 'completed'
            sync_log.finished_at = timezone.now()
            sync_log.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully synced {len(events_data)} events. "
                    f"New: {new_count}, Updated: {updated_count}"
                )
            )

        except Exception as e:
            sync_log.status = 'failed'
            sync_log.save()
            self.stderr.write(self.style.ERROR(f"Sync failed: {str(e)}"))
            raise