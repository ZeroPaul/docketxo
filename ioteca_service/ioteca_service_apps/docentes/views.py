from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import CategoriaDocente
from ioteca_service_apps.utils.permissions import ModelPermission

# Create your views here.

class CategoriaDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDocente

class CategoriaDocenteViewSet(viewsets.ModelViewSet):
    queryset = CategoriaDocente.objects.all()
    serializer_class = CategoriaDocenteSerializer
#    permission_classes = [ModelPermission, ]

