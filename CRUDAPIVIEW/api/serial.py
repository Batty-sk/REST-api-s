from rest_framework.serializers import ModelSerializer
from .models import Users
from rest_framework import serializers
class UserSerial(ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

#validations run when we use is_valid()
    def validate_crush(self, val):
        if val=='vaishnavi':
            raise serializers.ValidationError("Enter Some Other Name Because She's sk's girl 💕");
        return val;
