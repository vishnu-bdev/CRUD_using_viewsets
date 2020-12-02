from django.urls import path, include
from rest_framework import routers
from . views import StudentViewset


router  = routers.DefaultRouter()
router.register('student', StudentViewset)

urlpatterns = [
    
    path('api/', include(router.urls))
]


# Inside router we have:

# url inside router :== localhost:port_no/api/

# GET             - list      - localhost:port_no/api/employee
#                 - retrive   - localhost:port_no/api/employee/id

# POST, UPDATE or PUT, DELETE.
