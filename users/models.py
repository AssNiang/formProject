from django.db import models

# Create your models here.
class User(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"

class Professeur(User):
    contact_prof = models.CharField(max_length=15)
    date_d_adhesion = models.DateField(default='')
    chef_departement = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Prof'
        verbose_name_plural = "Profs"