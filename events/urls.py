
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RegisterAttendeeView, EventAttendeesView

router = DefaultRouter()
router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
    path('events/<int:event_id>/register/', RegisterAttendeeView.as_view(), name='register-attendee'),
    path('events/<int:event_id>/attendees/', EventAttendeesView.as_view(), name='event-attendees'),
]
    