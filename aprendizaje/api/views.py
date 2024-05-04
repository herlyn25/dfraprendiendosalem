from rest_framework.viewsets import ModelViewSet

from aprendizaje.api.serializers import NumerosSerializer
from aprendizaje.models import Numeros

class NumerosViewSet(ModelViewSet):
    queryset = Numeros.objects.all().order_by('representacion')
    serializer_class = NumerosSerializer