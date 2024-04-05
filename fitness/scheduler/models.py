from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(
        max_length=20, choices=USER_ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username


class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    gyms = models.ManyToManyField(Gym, related_name='trainers')


class Appointment(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Schedule(models.Model):
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name='schedules')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
