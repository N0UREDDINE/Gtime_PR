from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime, time
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier for authentication.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # This will hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class Role(models.Model):
    ADMIN = 'admin'
    SUPERVISOR = 'supervisor'
    EMPLOYEE = 'employee'

    # ROLE_CHOICES = [
    #     (ADMIN, _('Admin')),
    #     (SUPERVISOR, _('Supervisor')),
    #     (EMPLOYEE, _('Employee')),
    # ]

    name = models.CharField(
        max_length=50,
        default=EMPLOYEE,
        unique=True,  # Ensure role names are unique
    )

    def __str__(self):
       return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that uses email instead of a username.
    """
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    prime = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    
    is_staff = models.BooleanField(default=False)  # Required for admin login
    is_active = models.BooleanField(default=True)  # Required for user login

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email

class TimeTrack(models.Model):
    """
    Model to track the time of user activities.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='time_tracks')
    date = models.DateField(auto_now_add=True)
    login_time = models.TimeField()  # Captured at the moment of user login
    logout_time = models.TimeField(blank=True, null=True)  # Captured at the moment of user logout
    service_duration = models.DurationField(blank=True, null=True)  # Calculated duration
    break_duration = models.DurationField(blank=True, null=True)  # Calculated duration
    delay_time = models.DurationField(blank=True, null=True)  # Calculated duration

    def calculate_timings(self):
        # Calculate service_duration as the time between login and logout
        if self.logout_time:
            self.service_duration = self.logout_time - self.login_time
        else:
            self.service_duration = timezone.now() - self.login_time
        
        # Delay time calculation based on a company-wide defined start time
        work_start_time = timezone.make_aware(datetime.combine(self.date, time(8, 30)))
        self.delay_time = max(self.login_time - work_start_time, timezone.timedelta(0))

        # Ensure that delay_time is non-negative
        if self.delay_time.total_seconds() < 0:
            self.delay_time = timezone.timedelta(0)


        # Calculate break_duration based on user-submitted data or another mechanism

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now().date()
        self.calculate_timings()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.email} - {self.date}"

    class Meta:
        ordering = ['-date', '-login_time']
