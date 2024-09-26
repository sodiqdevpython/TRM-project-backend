
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    RoomsEquipmentView, 
    OverallClassesView, 
    OrganizationsView, 
    UserProfileView,
    RoomsTypeView,
    DistrictsView,
    RegionsView, 
    CitiesView, 
    RoomsView,

    CalculateSchoolStatistics,

    TestView
)

routerRoomsEquipmentView = SimpleRouter()
routerRoomsEquipmentView.register(r'', RoomsEquipmentView)

routerOverallClassesView = SimpleRouter()
routerOverallClassesView.register(r'', OverallClassesView)

routerOrganizationsView = SimpleRouter()
routerOrganizationsView.register(r'', OrganizationsView)

routerRoomsTypeView = SimpleRouter()
routerRoomsTypeView.register(r'', RoomsTypeView)

routerDistrictsView = SimpleRouter()
routerDistrictsView.register(r'', DistrictsView)

routerRegionsView = SimpleRouter()
routerRegionsView.register(r'', RegionsView)

routerCitiesView = SimpleRouter()
routerCitiesView.register(r'', CitiesView)

routerRoomsView = SimpleRouter()
routerRoomsView.register(r'', RoomsView)

routerUserProfileView = SimpleRouter()
routerUserProfileView.register(r'', UserProfileView)

# URL patterns
urlpatterns = [
    path('rooms-equipment/', include(routerRoomsEquipmentView.urls)),
    path('overall-classes/', include(routerOverallClassesView.urls)),
    path('organizations/', include(routerOrganizationsView.urls)),
    path('rooms-type/', include(routerRoomsTypeView.urls)),
    path('districts/', include(routerDistrictsView.urls)),
    path('regions/', include(routerRegionsView.urls)),
    path('cities/', include(routerCitiesView.urls)),
    path('rooms/', include(routerRoomsView.urls)),
    path('profile/', include(routerUserProfileView.urls)),

    path('organizations-statistics/', CalculateSchoolStatistics.as_view()),

    path('test/', TestView.as_view())
]
