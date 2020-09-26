from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='events-auth'),
    path('home/', views.home, name='events-home'),
    path('discover/', views.discover, name='events-discover'),
    path('calendar/', views.calendar, name='events-calendar'),
    path('all-events/', views.all, name='events-all'),
    path('about/', views.about, name='events-about'),
]