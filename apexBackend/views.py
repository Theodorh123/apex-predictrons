from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# import the serializer class for prediction
from apexBackend.serializers import PredictionSerializer
# importing prediction model
from apexBackend.models import Prediction

# Create your views here.

# creating serializer view for prediction
class PredictionListView(ListCreateAPIView):
    """
      class to retrieve the list of all predictions
    """
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()

class PredictionDetailView(RetrieveUpdateDestroyAPIView):
     """
     api view to retrieve, update and delete a prediction

     """
     serializer_class = PredictionSerializer
     queryset = Prediction.objects.all()    