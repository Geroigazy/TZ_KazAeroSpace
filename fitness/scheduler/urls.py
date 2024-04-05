from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name='user-detail'),
    path('trainers/', views.TrainerListCreate.as_view(), name='trainer-list-create'),
    path('trainers/<int:pk>/', views.TrainerDetail.as_view(), name='trainer-detail'),
    path('gyms/', views.GymListCreate.as_view(), name='gym-list-create'),
    path('gyms/<int:pk>/', views.GymDetail.as_view(), name='gym-detail'),
    path('schedules/', views.ScheduleListCreate.as_view(), name='schedule-list-create'),
    path('schedules/<int:pk>/', views.ScheduleDetail.as_view(), name='schedule-detail'),
    path('appointments/', views.AppointmentListCreate.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
]
