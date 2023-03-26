from django.urls import path
from .views import CRUD
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns=[
    path('api/',CRUD.as_view()),
    path('api/<int:id>/',CRUD.as_view()),
    path('authtoken/',ObtainAuthToken.as_view()),

]