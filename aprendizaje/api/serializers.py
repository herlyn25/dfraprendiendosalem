from rest_framework import serializers
from aprendizaje.models import Numeros

class NumerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numeros
        fields = ["familia", "representacion", "descripcion"]