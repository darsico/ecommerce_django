from django import views
from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.

class PostPagosView(generics.CreateAPIView):
    queryset = models.Pagos.objects.all()
    serializer_class = serializers.CreditoSerializer

class GetPagosView(generics.ListAPIView):
    queryset = models.Pagos.objects.filter(cantidad__gte=12, status=True)
    # queryset = models.Pagos.objects.all()
    serializer_class = serializers.CreditoSerializer