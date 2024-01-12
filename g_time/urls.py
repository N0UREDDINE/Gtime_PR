from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, CustomUserViewSet, TimeTrackSearchAPIView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'custom-users', CustomUserViewSet)
# Note: For TimeTrackSearchViewSet, you might not use a router if it's a simple API view

urlpatterns = [
    path('', include(router.urls)),  # This line will include the URL patterns for the RoleViewSet and CustomUserViewSet
    path('time-track-search/', TimeTrackSearchAPIView.as_view(), name='time-track-search'),
]
