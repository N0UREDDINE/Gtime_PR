from rest_framework import serializers
from .models import CustomUser, TimeTrack

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'phone', 'salaire', 'prime', 'role']



class TimeTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTrack
        fields = ['user', 'date', 'login_time', 'logout_time', 'service_duration', 'break_duration', 'delay_time']
