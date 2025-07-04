from datetime import datetime

import requests
from django.conf import settings


class EventsProviderClient:
    BASE_URL = "https://events.k3scluster.tech/api/events/"

    def get_events(self, date_filter=None):
        params = {}
        if date_filter:
            if isinstance(date_filter, datetime):
                date_filter = date_filter.date()
            params['changed_at'] = date_filter.strftime('%Y-%m-%d')

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()