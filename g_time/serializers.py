from rest_framework import serializers
from .models import CustomUser, TimeTrack, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'phone', 'salaire', 'prime', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with hashed password
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            salaire=validated_data['salaire'],
            prime=validated_data['prime'],
            role=validated_data.get('role')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Update user except for password
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Update the password if provided
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance



class TimeTrackSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)  # Assuming the user has an attribute 'name'
    
    class Meta:
        model = TimeTrack
        fields = ['user_name', 'date', 'login_time', 'logout_time', 'service_duration', 'break_duration', 'delay_time']