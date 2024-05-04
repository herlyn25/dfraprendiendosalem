from django.contrib import admin
from aprendizaje.models import *

# Register your models here.
@admin.register(Numeros)
class NumerosAdmin(admin.ModelAdmin):
    list_display = ["representacion", "descripcion","familia"]
    

@admin.register(Letras)
class LetrasAdmin(admin.ModelAdmin):
    list_display = ["representacion","descripcion"]
    
