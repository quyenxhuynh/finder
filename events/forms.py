from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Event


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_date', 'event_time', 'event_address', 
        'event_latitude', 'event_longitude', 'event_banner', 'event_tags']

