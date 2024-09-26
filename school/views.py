
import time
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import (
    OrganizationStatistics,
    OverallClasses,
    RoomsEquipment,
    Organizations,
    UserProfile,
    RoomsType,
    Districts, 
    Regions,
    Cities,
    Rooms
)

from .serializers import (
    RoomsEquipmentSerializer,
    OverallClassesSerializer,
    CustomRegisterSerializer,
    OrganizationsSerializer,
    UserProfileSerializer,
    RoomsTypeSerializer,
    DistrictsSerializer,
    RegionsSerializer, 
    CitiesSerializer,
    RoomsSerializer,

    SchoolStatisticsSerializer
)

from .filters import OrganizationsFilter


class RoomsEquipmentView(ModelViewSet):
    queryset = RoomsEquipment.objects.all()
    serializer_class = RoomsEquipmentSerializer

class OverallClassesView(ModelViewSet):
    queryset = OverallClasses.objects.all()
    serializer_class = OverallClassesSerializer

class OrganizationsView(ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationsFilter

class RoomsTypeView(ModelViewSet):
    queryset = RoomsType.objects.all()
    serializer_class = RoomsTypeSerializer

class DistrictsView(ModelViewSet):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['region']

class RegionsView(ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer

class CitiesView(ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['region']

class RoomsView(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class CalculateSchoolStatistics(APIView):

    def get(self, request):
        get_statistics = OrganizationStatistics.objects.all().order_by('id')
        get_statistics = SchoolStatisticsSerializer(get_statistics, many=True)

        context = {
            "data": get_statistics.data,
        }
        return Response(context)

class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_active', 'is_selected', 'is_super_admin']

    search_fields = ['first_name', 'last_name']


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save(request)
            return Response({
                'id': user.id,
                'username': user.username
            })
        else:
            return Response(serializer.errors, status=400)
        
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class TestView(APIView):
    
    def get(self, request):
        data = get_object_or_404(User, id=request.user.id)
        print(data)
        user = UserSerializer(data)
        print(request.user)
        context = {
            'user': user.data
        }
        return Response(context)
        
        
    # def list(self, request, *args, **kwargs):
    #     time.sleep(2)  # 2-second kechiktirish
    #     return super().list(request, *args, **kwargs)