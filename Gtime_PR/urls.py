from django.contrib import admin
from django.urls import path, include 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")


urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/', include('g_time.urls')),  

]
