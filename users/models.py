from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Opções de Daltonismo
    COLOR_BLIND_CHOICES = [
        ('none', 'Nenhum'),
        ('protanopia', 'Protanopia'),
        ('deuteranopia', 'Deuteranopia'),
        ('tritanopia', 'Tritanopia'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=5, default='pt')
    color_blind_mode = models.CharField(max_length=20, choices=COLOR_BLIND_CHOICES, default='none')
    high_contrast = models.BooleanField(default=False)
    font_size_scale = models.FloatField(default=1.0) # Ex: 1.0 (100%), 1.5 (150%)

    def __str__(self):
        return f"Perfil de {self.user.username}"