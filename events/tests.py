from django.test import TestCase
from events.models import Event, Profile
import datetime
import tempfile

# Create your tests here.

#example
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
    
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

#events model test cases
class EventsTestCases(TestCase):
    def setUp(self):
        Event.objects.create(event_name="Test")

    def test_events_name(self):
        test_event = Event.objects.get(event_name="Test")
        self.assertEqual(test_event.event_name, "Test")

    #edge case
    def test_events_NoDescription(self):
        test_event = Event.objects.get(event_name="Test")
        self.assertEqual(test_event.event_description, None)
    
    #edge case
    def test_events_NoDate(self):
        test_event = Event.objects.get(event_name="Test")
        self.assertEqual(test_event.event_date, None)
    
    #edge case
    def test_events_NoTime(self):
        test_event = Event.objects.get(event_name="Test")
        self.assertEqual(test_event.event_time, None)
    
    #edge case
    def test_events_NoTags(self):
        test_event = Event.objects.get(event_name="Test")
        self.assertEqual(test_event.event_tags, None)

class EventsTestCasesTwo(TestCase):
    def setUp(self):
        Event.objects.create(event_name="Event2",event_description="This is an event")

    #test showing that the event description is properly stored in the database
    def test_events_description(self):
        test_event = Event.objects.get(event_name="Event2")
        self.assertEqual(test_event.event_description, "This is an event")

class EventsTestCaseThree(TestCase):
    def setUp(self):
        Event.objects.create(event_name="Event2",event_description="This is an event", event_date=datetime.date(2020, 11, 3), event_tags="#eventname", event_banner=None, event_time=datetime.time(12, 45, 0))
    
    #test showing that when the event description is changed, it is properly stored in the database
    def test_events_change_description(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_description="This is an updated description.")
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_description, "This is an updated description.")
    
    #test showing that when the event description is removed, it is properly stored as an empty string
    def test_events_delete_description(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_description="")
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_description, "")

    #test showing that when an event date is changed, it is storred in the database
    def test_events_change_date(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_date=datetime.date(2022, 1, 8))
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_date, datetime.date(2022, 1, 8))

    #test showing that when the event date is removed, it is properly stored in the database
    def test_events_remove_date(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_date=None)
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_date, None)
    
    #test showing that when an event tag is changed, it is storred in the database
    def test_events_change_tags(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_tags="#eventone#eventtwo#eventthree")
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_tags, "#eventone#eventtwo#eventthree")

    #test showing that when the event tags are removed, it is properly stored in the database
    def test_events_remove_tags(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_tags="")
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_tags, "")
    
    #test showing that when the event banner is added, it is properlys tored in the database
    #a temporary file is used to test this feature, testing jpg
    def test_events_banner(self):
        test_event = Event.objects.get(event_name="Event2")
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        Event.objects.filter(pk=test_event.pk).update(event_banner=image)
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_banner, image)
    
    #testing jpeg
    def test_events_banner_two(self):
        test_event = Event.objects.get(event_name="Event2")
        image = tempfile.NamedTemporaryFile(suffix=".jpeg").name
        Event.objects.filter(pk=test_event.pk).update(event_banner=image)
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_banner, image)
    
    #testing png
    def test_events_two_banner_three(self):
        test_event = Event.objects.get(event_name="Event2")
        image = tempfile.NamedTemporaryFile(suffix=".png").name
        Event.objects.filter(pk=test_event.pk).update(event_banner=image)
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_banner, image)
    
    #test showing that whent the event banner is deleted, it is properly stored in the databse
    def test_events_remove_banner(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_banner=None)
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_banner, None)
    
    #test showing that when the event time is changed, it is properly stored in the databse
    def test_events_time(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_time=datetime.time(5, 30, 0))
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_time, datetime.time(5, 30, 0))
    
    #test showing that when the event time is deleted, it is properly stored in the databse
    def test_events_remove_time(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_time=None)
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_time, None)
    
    #test the occurance of an empty string event name
    def test_event_remove_name(self):
        test_event = Event.objects.get(event_name="Event2")
        Event.objects.filter(pk=test_event.pk).update(event_name="")
        test_event.refresh_from_db()
        self.assertEqual(test_event.event_name, "")

