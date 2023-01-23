from .models import *
from rest_framework import serializers




class ScheduleDeviceSerializer(serializers.Serializer):
    Devicename = serializers.CharField(required=True)
    temp = serializers.CharField(required=True)
    hum = serializers.CharField(required=True)
    bat = serializers.CharField(required=True)
    ppm = serializers.CharField(required=True)
    sol = serializers.CharField(required=True)
    Timestamp = serializers.CharField(required=True)