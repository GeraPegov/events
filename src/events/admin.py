from django.contrib import admin

# Register your models here.
from .models import Event, Place

admin.site.register(Event)
admin.site.register(Place)