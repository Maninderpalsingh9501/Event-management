
from rest_framework import serializers
from .models import Event, Attendee


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['id', 'name', 'email']


class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    