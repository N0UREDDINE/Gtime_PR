from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import TimeTrack, Role, CustomUser
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Q
from .serializers import TimeTrackSerializer, RoleSerializer, CustomUserSerializer

class TimeTrackSearchAPIView(APIView):
    def get(self, request):
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        name = request.query_params.get('name')
        queryset = TimeTrack.objects.all()

        if year and month:
            queryset = queryset.annotate(year=TruncYear('date'), month=TruncMonth('date'))
            queryset = queryset.filter(year__year=year, month__month=month)

        if name:
            queryset = queryset.filter(user__name__icontains=name)

        serializer = TimeTrackSerializer(queryset, many=True)
        return Response(serializer.data)




        
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer