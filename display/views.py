from django.shortcuts import render
from .models import (
    Video,
    Categoria
)

# Create your views here.
def videos(request):
    videos=Video.objects.all()
    categorias = Categoria.objects.all()
    categoria = request.GET.get('cat')
    if categoria:
        try:
            categorias_filter=[categoria.id for categoria in Categoria.objects.filter(nome=categoria)]
            videos=videos.filter(categorias__in=categorias_filter)
        except:
            pass

    return render(
        request,
        'videos.html',
        {
            'categorias': categorias,
            'videos': videos
        }
    )

def video(request, id):
    categorias = Categoria.objects.all()
    videos=Video.objects.all()
    video=Video.objects.get(id=id)

    return render(
        request,
        'video.html',
        {
            'categorias': categorias,
            'video': video,
            'videos': videos,
        }
    )