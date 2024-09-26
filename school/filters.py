import django_filters
from utils.choices import OrganizationsType, OrganizationsRatingType
from .models import Organizations, Districts, Cities, Regions

class OrganizationsFilter(django_filters.FilterSet):
    region = django_filters.ModelChoiceFilter(queryset=Regions.objects.all())
    district = django_filters.ModelChoiceFilter(queryset=Districts.objects.all())
    city = django_filters.ModelChoiceFilter(queryset=Cities.objects.all())
    is_city = django_filters.BooleanFilter()
    is_inclusive = django_filters.BooleanFilter()
    education_type = django_filters.ChoiceFilter(choices=OrganizationsType.choices)
    rating = django_filters.ChoiceFilter(choices=OrganizationsRatingType.choices)

    class Meta:
        model = Organizations
        fields = ['region', 'district', 'city', 'is_city','rating' ,'is_inclusive', 'education_type']
