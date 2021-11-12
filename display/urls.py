from django.urls import include, path

from .views import (
    videos,
    video
)
urlpatterns = [
    path('', videos, name='videos'),
    path('<int:id>/', video, name='video'),
]