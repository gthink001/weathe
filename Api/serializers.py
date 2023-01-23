from .models import *
from rest_framework import serializers




class ScheduleDeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    action = serializers.CharField(required=True)
    fire_date = serializers.DateTimeField(required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)