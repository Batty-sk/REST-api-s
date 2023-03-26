from django.db import models
from rest_framework.serializers import ModelSerializer
# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=100)
    crush=models.CharField(max_length=100)
    phone=models.IntegerField(verbose_name='no',unique=True) #verbose name is display as label of field in forms and admin panel.

    def __str__(self):
        return self.name;