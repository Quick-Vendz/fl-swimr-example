# urls
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', front_view, name='front_view'),    
    path('classes/', classes_view, name='classes_view'),
    path('instructors/', instructors_view, name='instructors_view'),
    path('my-bookings/', my_bookings_view, name='my_bookings_view'),
    path('weekly-schedule/', weekly_schedule_view, name='weekly_schedule_view'),
]