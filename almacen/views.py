from django import views
from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
# Create your views here.
class PostAlmacenView(generics.CreateAPIView):
	queryset = models.Almacen.objects.all()
	serializer_class = serializers.AlmacenSerializer

class GetAlmacenView(generics.ListAPIView):
	queryset = models.Almacen.objects.all()
	serializer_class = serializers.AlmacenSerializer
