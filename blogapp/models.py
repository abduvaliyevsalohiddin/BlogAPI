from django.db import models
from django.contrib.auth.models import AbstractUser


class Muallif(AbstractUser):
    ism = models.CharField(max_length=30, blank=True)
    yosh = models.PositiveSmallIntegerField(null=True, blank=True)
    kasb = models.CharField(max_length=30, blank=True)

    first_name = None
    last_name = None

    def __str__(self):
        return self.ism


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=30)
    matn = models.TextField()
    sana = models.DateField()
    korish_soni = models.PositiveSmallIntegerField(default=0)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
