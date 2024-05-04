from rest_framework.routers import DefaultRouter
from aprendizaje.api.views import NumerosViewSet

router = DefaultRouter()
router.register('numeros', NumerosViewSet)