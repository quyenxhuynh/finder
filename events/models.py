from django.db import models
from django import forms
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import reverse

class Event(models.Model):
    event_organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event_name = models.CharField(max_length = 64)
    event_description = models.TextField(max_length = 500, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)
    event_banner = models.ImageField(null=True, blank=True)
    event_tags = models.CharField(null=True, blank=True, max_length = 100)
    
    date_posted = models.DateTimeField(auto_now_add=True)

    @property
    def get_username(self):
        return self.event_organizer.username

    def get_absolute_url(self): 
        return reverse('events:all-events')

    def __str__(self):
        return self.event_name 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default_pfp.png", upload_to="profile_pics")
    slug = models.SlugField(unique=False, null=True) #should be unique, these fields are added to allow for code to be merged with the existing database. call save to make correct slugs
    favorites = models.ManyToManyField(Event, related_name='favorited_by')
    rsvped = models.ManyToManyField(Event, related_name='rsvped_by')

    def __str__(self):
       return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
