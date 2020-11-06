# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.auth, name='events-auth'),
#     path('home/', views.home, name='events-home'),
#     path('discover/', views.discover, name='events-discover'),
#     path('calendar/', views.calendar, name='events-calendar'),
#     path('all-events/', views.all, name='events-all'),
#     path('about/', views.about, name='events-about'),
# ]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import AllPostsListView, PostDetailView, EventCreateView, EventUpdateView, EventDeleteView, ProfileDetailView, ProfileListView

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),

    path('all-events/', views.all_events, name="all-events"),
    path('saved-events/', views.saved_events, name="saved-events"),

    path('new-event/', EventCreateView.as_view(), name="new-event"),
    path('posts/<int:pk>/update/', EventUpdateView.as_view(), name="update-event"),
    path('posts/<int:pk>/delete/', EventDeleteView.as_view(), name="delete-event"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='individual-event'),

    path('posts/<int:pk>/favorite/', views.favorite, name='fav-event'),
    path('posts/<int:pk>/unfavorite/', views.unfavorite, name='unfav-event'),
    path('posts/<int:pk>/rsvp/', views.rsvp, name='rsvp-event'),
    path('posts/<int:pk>/unrsvp/', views.unrsvp, name='unrsvp-event'),

    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name="profile"),
    #path('people/', ProfileListView.as_view(), name="all-profiles"),
]