from rest_framework import serializers
from .models import CustomUser, Trainer, Gym, Schedule, Appointment


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role'] 

class TrainerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer() 

    class Meta:
        model = Trainer
        fields = '__all__'

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer() 

    class Meta:
        model = Schedule
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    client = CustomUserSerializer() 
    trainer = TrainerSerializer()  

    class Meta:
        model = Appointment
        fields = '__all__'

