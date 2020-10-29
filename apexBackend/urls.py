from django.urls import path
from apexBackend.views import PredictionListView, PredictionDetailView

urlpatterns = [
    path('prediction/<uuid:pk/', PredictionDetailView.as_view(), name="prediction-detail"),
    path('prediction/', PredictionListView.as_view(), name="prediction-list"),
]
