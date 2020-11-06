import django_filters
from django_filters import CharFilter
from django.db.models import Q
from .models import *


class EventFilter(django_filters.FilterSet):
    event_name = CharFilter('event_name', 'icontains', label='event_name')
    event_description = CharFilter('event_description', 'icontains', label="event_description")
    event_tags = CharFilter('event_tags', 'icontains', label="event_tags")

    class Meta:
        model = Event
        fields = ['event_name', 'event_organizer', 'event_description', 
        'event_date', 'event_time', 'event_tags']
