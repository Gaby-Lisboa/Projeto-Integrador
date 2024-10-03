from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers # app_smart é o app criado.
from rest_framework.response import Response
from rest_framework import status
from ..models import Sensor, TemperaturaData, UmidadeData, LuminosidadeData # o .. é para voltar dois níveis para encontrar o arquivo models.py
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter, TemperaturaDataFilter
from django_filters.rest_framework import DjangoFilterBackend


class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    #permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter

class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializer
    #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperaturaDataFilter

class UmidadeDataViewSet(viewsets.ModelViewSet):
    queryset = UmidadeData.objects.all()
    serializer_class = serializers.UmidadeDataSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class LuminosidadeDataViewSet(viewsets.ModelViewSet):
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializers.LuminosidadeDataSerializer
    #permission_classes = [permissions.IsAuthenticated]