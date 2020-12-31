# Finder
Finder is a social justice app created to help organize meet-ups and protests...

### Features
- create new protest or meetup events
  - include a banner, tags, and event information
- view nearby events through an interactive map
- favorite, rsvp, and share events

### External APIs 
- OAuth: secure login
- Google Places API: display map/autocomplete

### Install and Run
Install Django dependencies:  
`pip install -r requirements.txt`  
Initialize database tables:  
`python manage.py migrate`  
Create a super-user for the admin:  
`python manage.py createsuperuser`  
Run the application  
`python manage.py runserver`  
