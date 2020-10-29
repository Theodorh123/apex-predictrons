from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from apexBackend.models import Prediction
from rest_framework.response import Response
from django.contrib.auth.models import User

# getting the custom user model


# defining custom serializer

class CustomUserSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','username','email','password')

# serializer for prediction
class PredictionSerializer(serializers.ModelSerializer):
    serializers.ImageField(required=True, allow_null=False)
    class Meta:
        model = Prediction
        fields = ('physician','patient_name','xray_image','prediction')
  