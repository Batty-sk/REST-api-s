from .views import CountryCurrency
from django.urls import path
urlpatterns=[
    path('Cf/<str:country>/',CountryCurrency.as_view(),name='CountryCurrency'),
    path('Cf/',CountryCurrency.as_view(),name='AllCountries'),
]