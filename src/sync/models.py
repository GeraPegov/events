from django.db import models


class SyncLog(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    date_filter = models.DateField(null=True, blank=True)
    sync_all = models.BooleanField(default=False)
    new_events = models.PositiveIntegerField(default=0)
    updated_events = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default='running')

    class Meta:
        ordering = ['-started_at']

        
class Event(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    place = models.CharField(max_length=255)
    changed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name