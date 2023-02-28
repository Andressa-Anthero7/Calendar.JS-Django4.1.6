from django.db import models

# Create your models here.


class Agendamento(models.Model):
    title = models.CharField(max_length=10)
    data = models.CharField(max_length=50)


