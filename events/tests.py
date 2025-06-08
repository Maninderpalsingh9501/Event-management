
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Event

class EventTests(APITestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name='Test Event',
            location='Online',
            start_time='2030-01-01T10:00:00Z',
            end_time='2030-01-01T12:00:00Z',
            max_capacity=2
        )

    def test_create_event(self):
        data = {
            'name': 'New Event',
            'location': 'Delhi',
            'start_time': '2030-01-01T10:00:00Z',
            'end_time': '2030-01-01T12:00:00Z',
            'max_capacity': 5
        }
        response = self.client.post(reverse('events-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_attendee(self):
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(reverse('register-attendee', args=[self.event.id]), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    