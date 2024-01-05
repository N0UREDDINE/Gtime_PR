from django.urls import path
from .views import logout_time_track

urlpatterns = [
    # ... other url patterns
    path('api/timetrack/logout/', logout_time_track, name='logout_time_track'),
]
