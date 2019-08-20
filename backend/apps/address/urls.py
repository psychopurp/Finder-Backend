from django.urls import path
from address.views import get_provinces, get_cities, get_schools, get_majors

ADDRESS_URL = [
    path('api/get_provinces/', get_provinces, name='get_provinces'),
    path('api/get_cities/', get_cities, name='get_cities'),
    path('api/get_schools/', get_schools, name='get_schools'),
    path('api/get_majors/', get_majors, name='get_majors')
]
