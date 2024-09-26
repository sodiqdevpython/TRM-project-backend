from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import (
    Regions, Districts, Cities, Organizations, 
    OverallClasses, RoomsType, RoomsEquipment, 
    Rooms, OrganizationStatistics, UserProfile
)
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class CustomRegisterSerializer(RegisterSerializer):
    id = serializers.ReadOnlyField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        return data

    def save(self, request):
        user = super().save(request)
        return user

class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    
    class Meta:
        model = UserProfile
        fields = ['id','first_name', 'last_name', 'father_name', 'passport_id', 'manzil', 'pinfl', 'position', 'tel_number', 'command_pdf', 'command_expire','is_active', 'born_in', 'is_selected', 'is_super_admin', 'user', 'created']

class SchoolStatisticsSerializer(serializers.ModelSerializer):

    count_data = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationStatistics
        fields = ['type', 'number', 'count_data']

    def get_count_data(self, instance):
        count_data = Organizations.objects.filter(education_type=instance.type).count()
        
        return count_data


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['id', 'name']


class DistrictsSerializer(serializers.ModelSerializer):
    region = RegionsSerializer()

    class Meta:
        model = Districts
        fields = ['id', 'region', 'name']


class CitiesSerializer(serializers.ModelSerializer):
    region = RegionsSerializer()

    class Meta:
        model = Cities
        fields = ['id', 'region', 'name']


class OrganizationsSerializer(serializers.ModelSerializer):
    district = DistrictsSerializer()
    city = CitiesSerializer()
    region = RegionsSerializer()
    admin = UserSerializer()

    class Meta:
        model = Organizations
        fields = ['id','organization_number', 'name', 'education_type', 'power', 'vr_mode_url', 
                  'is_inclusive', 'rating','ball', 'district', 'city','is_city','region', 'admin']


class OverallClassesSerializer(serializers.ModelSerializer):
    organization = OrganizationsSerializer()

    class Meta:
        model = OverallClasses
        fields = ['id', 'organization', 'name', 'rooms_amount']


class RoomsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsType
        fields = ['id', 'name']

class RoomsEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsEquipment
        fields = ['id', 'name', 'measure_type', 'amount', 'avilable_type', 
                  'accepted_date', 'entered_date', 'when_first_time_used', 
                  'when_made', 'image1', 'image2', 'image3', 'penny_by_year', 
                  'xarakteri', 'equipment_type']


class RoomsSerializer(serializers.ModelSerializer):
    room_category = RoomsTypeSerializer()
    room_uquipment = RoomsEquipmentSerializer(many=True)

    class Meta:
        model = Rooms
        fields = ['id', 'room_category', 'students_amount', 'room_uquipment']