from django.db import models

class Usuario(model.Models):
    nome = models.Charfield(max_length=100)


