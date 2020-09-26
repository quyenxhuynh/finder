from django.shortcuts import render

events = [
    { 
        'name':'event 1 name',
        'date':'thu, feb 11',
        'description':'this is the event description.'
    },
    {
        'name':'event 2 name',
        'date':'date',
        'description':'this is the event description.'
    }
]

def auth(request):
    # if authenticated then render(request, 'events/home.html') else
    return render(request, 'events/auth.html')

def home(request):
    return render(request, 'events/home.html')

def discover(request):
    return render(request, 'events/discover.html')

def calendar(request):
    return render(request, 'events/calendar.html')

def discover(request):
    return render(request, 'events/discover.html')

def all(request):
    context = {
        'events':events,
        'title':'All Events'
    }
    return render(request, 'events/all-events.html', context)

def about(request):
    return render(request, 'events/about.html')


