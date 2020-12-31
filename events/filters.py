import django_filters
from django_filters import CharFilter
from .models import *


class EventFilter(django_filters.FilterSet):
    event_name = CharFilter('event_name', 'icontains', label='event_name')
    event_description = CharFilter('event_description', 'icontains', label="event_description")
    event_location = CharFilter('event_location', 'icontains', label='event_location')
    event_tags = CharFilter('event_tags', 'icontains', label="event_tags")

    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_date', 'event_time', 'event_location', 
        'event_latitude', 'event_longitude', 'event_tags']
