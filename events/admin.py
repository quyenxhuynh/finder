from django.contrib import admin
from .models import Event, Profile

# class EventAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
#     }
    
admin.site.register(Event)
admin.site.register(Profile)
