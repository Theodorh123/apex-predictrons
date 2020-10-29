from rest_framework import serializers
from .models import User, AbstractUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'sex', 'date_of_birth', 'occupation')