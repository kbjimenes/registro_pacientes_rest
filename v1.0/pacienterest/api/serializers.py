from rest_framework import serializers
from . import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        	'id',
            'nombres',
            'apellidos',
            'telefono',
            'date_added'
        )
        model = models.Paciente