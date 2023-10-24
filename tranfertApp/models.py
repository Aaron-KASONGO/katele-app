from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Etudiant(models.Model):
    nom_etudiant = models.CharField(max_length=30)
    post_nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.IntegerField()
    matricule = models.CharField(max_length=20)
    login = models.CharField(max_length=30)
    password = models.TextField()


class Universite(User):
    nom_universite = models.CharField(max_length=30)
    adresse = models.TextField()
    contact = models.CharField(max_length=30)
    website = models.TextField()

    def __str__(self):
        return self.nom_universite
    

class Palmares(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    annee = models.IntegerField()
    universite = models.ForeignKey('Universite', on_delete=models.CASCADE)

class Etude(models.Model):
    promotion = models.CharField(max_length=30)
    palmares = models.ForeignKey('Palmares', on_delete=models.CASCADE)
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)

class Inscription(models.Model):
    date_inscription = models.DateTimeField()
    faculte = models.CharField(max_length=30)
    promotion = models.CharField(max_length=30)
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)

class Parcous(models.Model):
    anne_acad = models.IntegerField()
    cote = models.IntegerField()
    mention = models.CharField(max_length=15)
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
