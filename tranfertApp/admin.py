from django.contrib import admin
from .models import Universite, Etude, Etudiant, Palmares, Parcous, Inscription

# Register your models here.
@admin.register(Universite)
class UniversiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Etude)
class EtudeAdmin(admin.ModelAdmin):
    pass

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    pass

@admin.register(Palmares)
class PalmaresAdmin(admin.ModelAdmin):
    pass

@admin.register(Parcous)
class ParcoursAdmin(admin.ModelAdmin):
    pass

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    pass