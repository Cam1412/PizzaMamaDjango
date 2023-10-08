from django.db import models
"""
le model permet de creer les champs de donnees de notre application et bd
"""
class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
