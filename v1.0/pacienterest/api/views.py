from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here
class ListPacientes(generics.ListCreateAPIView):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer

class DetailPaciente(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer