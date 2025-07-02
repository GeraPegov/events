from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    place_name = serializers.CharField(source='place.name', read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'status', 'place']