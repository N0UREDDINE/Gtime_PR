from django.contrib import admin
from .models import CustomUser, Role, TimeTrack



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'phone', 'salaire', 'prime', 'role']

@admin.register(TimeTrack)
class TimeTrackAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'login_time', 'logout_time', 'service_duration', 'break_duration', 'delay_time']
