from django.db import models
from .categoria import Categoria

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4']

    if not ext.lower() in valid_extensions:
        raise ValidationError('Somente arquivos .mp4 são válidos')

class Video(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=16
    )

    categorias = models.ManyToManyField(
        Categoria,
        verbose_name='Categorias'
    )

    publicado = models.BooleanField(
        verbose_name='Publicado',
        default=False
    )

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',
        upload_to='fotos_capa/',
        null=True
    )
    
    video = models.FileField(
		verbose_name="Vídeo",
		help_text='Adicione aqui o vídeo no formato .mp4',
		upload_to='videos/',
		blank=True, null=True,
        validators=[validate_file_extension]
	)

    url = models.URLField(
        verbose_name='URL',
        null=True, blank=False
    )
    
    def __str__(self):
        return self.nome