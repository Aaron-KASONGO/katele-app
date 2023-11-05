from django.forms import ModelForm
from django import forms
from .models import Palmares, Etudiant, Parcous

class PalmaresForm(ModelForm):
    class Meta:
        model = Palmares
        fields = ('annee','file_first_sem', 'file_second_sem')

class EtudiantForm(ModelForm):
    palmares = forms.IntegerField()
    promotion = forms.CharField(max_length=30)
    class Meta:
        model = Etudiant
        fields = ('nom_etudiant', 'post_nom', 'prenom', 'date_naissance', 'matricule', 'password', 'login', 'palmares', 'promotion')

class Parcoursform(ModelForm):
    class Meta:
        model = Parcous
        fields = ('anne_acad', 'file', 'cote', 'mention', 'promotion')
