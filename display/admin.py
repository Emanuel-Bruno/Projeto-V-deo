from django.contrib import admin
from display.models import (
    Categoria,
    Video
)

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome'
    ]

    search_fields = [
        'id',
        'nome'
    ]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'publicado'
    ]

    search_fields = [
        'id',
        'nome',
        'publicado',
        'categorias'
    ]
    
    autocomplete_fields = [
        'categorias'
    ]
