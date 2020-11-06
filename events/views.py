from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import EventFilter
from .forms import CreateUserForm, NewEventForm
from .models import Event, Profile

def index(request):
    if request.user.is_authenticated:
        return redirect('events:home')
    else:
        form = CreateUserForm()
        if request.method == "POST" and "signup" in request.POST:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                messages.success(request, "Account created!")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('events:home')
            else:
                context = {'reg_error': 'Invalid request. Try again!'}
                return render(request, 'events/index.html', context)
        
        elif (request.method == "POST") and ("signin" in request.POST):
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'events/home.html')
            else:
                context = {'login_error':'Invalid username and/or password.'}
                return render(request, 'events/index.html', context)
        else: 
            return render(request, 'events/index.html')

def home(request):
    return render(request, 'events/home.html')

def signin(request):
    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'events/home.html')
        else:
            context = {'login_error':'Invalid username and/or password.'}
            return render(request, 'events/signin.html', context)
    else: 
        return render(request, 'events/signin.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('events:home')
    else:
        form = CreateUserForm()
        if request.method == "POST" :
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                messages.success(request, "Account created!")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('events:home')
        return render(request, 'events/signup.html')


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'event_description', 'event_date', 'event_time', 'event_banner', 'event_tags']
    template_name = 'events/new-event.html'

    def form_valid(self, form):
        form.instance.event_organizer = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['event_name', 'event_description', 'event_date', 'event_time', 'event_banner', 'event_tags']
    template_name = 'events/update-event.html'
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.event_organizer = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.event_organizer:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/delete-event.html'
    context_object_name = 'post'

    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.event_organizer:
            return True
        return False

def signout(request):
    logout(request)
    return redirect('events:home')


def all_events(request):
    latest_events = Event.objects.all()
    myFilter = EventFilter(request.GET, queryset=latest_events)
    latest_events = myFilter.qs

    context = {'events':latest_events, 'eventFilter':myFilter}
    return render(request, 'events/all-events.html', context)

@login_required
def saved_events(request):
    saved = (request.user.profile.favorites.all() | request.user.profile.rsvped.all()).distinct()
    myFilter = EventFilter(request.GET, queryset=saved)
    saved = myFilter.qs

    favs = request.user.profile.favorites.all()
    rsvped = request.user.profile.rsvped.all()

    context = {'events':saved, 'eventFilter':myFilter, 'favorited_posts':favs, 'rsvped_posts':rsvped}
    return render(request, 'events/saved-events.html', context)

def favorite(request, pk): 
    post = Event.objects.get(pk=pk)
    request.user.profile.favorites.add(post)
    return HttpResponseRedirect(reverse('events:individual-event', args=(pk,)))

def unfavorite(request, pk): 
    post = Event.objects.get(pk=pk)
    request.user.profile.favorites.remove(post)
    return HttpResponseRedirect(reverse('events:individual-event', args=(pk,)))

def rsvp(request, pk): 
    post = Event.objects.get(pk=pk)
    request.user.profile.rsvped.add(post)
    return HttpResponseRedirect(reverse('events:individual-event', args=(pk,)))

def unrsvp(request, pk): 
    post = Event.objects.get(pk=pk)
    request.user.profile.rsvped.remove(post)
    return HttpResponseRedirect(reverse('events:individual-event', args=(pk,)))

class AllPostsListView(ListView):
    model = Event
    template_name = 'events/all-events.html'
    context_object_name = 'events'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Event
    template_name = 'events/individual-event.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['favorite_posts'] = self.request.user.profile.favorites.all()
        context['rsvped_posts'] = self.request.user.profile.rsvped.all()
        return context



@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'events/profile.html'
    slug_url_kwarg = "slug"
    context_object_name = 'profile'
    
class ProfileListView(ListView):
    model = Profile
    template_name = 'events/people.html'
    context_object_name = 'profiles'
    ordering = ['user.username']

