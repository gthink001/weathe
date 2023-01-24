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


class DeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)


class DeviceSchedulingSerializer(serializers.ModelSerializer):
    temp2 = serializers.CharField(source='temp')
    hum2 = serializers.CharField(source='hum')
    ppm2 = serializers.CharField(source='ppm')
    bat2 = serializers.CharField(source='bat')
    sol2 = serializers.CharField(source='sol')
    Timestamp2 = serializers.CharField(source='Timestamp')
    id = serializers.ReadOnlyField()

    class Meta:
        model = Scheduling
        fields = ('temp2', 'hum2', 'ppm2', 'bat2', 'sol2', 'Timestamp2', 'id')