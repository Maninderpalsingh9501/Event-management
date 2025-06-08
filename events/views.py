
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer, RegistrationSerializer
from django.shortcuts import get_object_or_404


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')


class RegisterAttendeeView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        if event.attendees.count() >= event.max_capacity:
            return Response({'error': 'Event is at full capacity.'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        if Attendee.objects.filter(event=event, email=data.get('email')).exists():
            return Response({'error': 'Attendee already registered with this email.'}, status=status.HTTP_400_BAD_REQUEST)

        attendee = Attendee.objects.create(
            event=event,
            name=data.get('name'),
            email=data.get('email')
        )
        return Response(AttendeeSerializer(attendee).data, status=status.HTTP_201_CREATED)


class EventAttendeesView(generics.ListAPIView):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        event = get_object_or_404(Event, id=self.kwargs['event_id'])
        return event.attendees.all()
    