from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Trainer)
admin.site.register(models.Appointment)
admin.site.register(models.Schedule)
admin.site.register(models.Gym)
