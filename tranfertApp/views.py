from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Etudiant, Palmares, Universite, Etude

from .forms import PalmaresForm, EtudiantForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    palmares = Palmares.objects.filter(universite=request.user)
    etudes = Etude.objects.filter(palmares__in=palmares, valide=True)
    etudes_invalid = Etude.objects.filter(palmares__in=palmares, valide=False)
    return render(request, 'transfertApp/dashboard.html', {'etudes': etudes, 'palmares': palmares, 'etudes_invalid': etudes_invalid})

@login_required(login_url='login')
def validated_etudiants(request):
    palmares = Palmares.objects.filter(universite=request.user)
    etudes = Etude.objects.filter(palmares__in=palmares, valide=True)
    return render(request, 'transfertApp/validatedEtudiants.html', {'etudes': etudes, 'palmares': palmares})

@login_required(login_url='login')
def invalidated_etudiants(request):
    palmares = Palmares.objects.filter(universite=request.user)
    etudes_invalid = Etude.objects.filter(palmares__in=palmares, valide=False)
    return render(request, 'transfertApp/invalidatedEtudiants.html', {'etudes_invalid': etudes_invalid, 'palmares': palmares})

@login_required(login_url='login')
def add_palmares(request):
    if request.method == 'POST':
        form = PalmaresForm(request.POST)
        if form.is_valid():
            palmares = form.save(commit=False)
            palmares.universite = Universite.objects.get(pk=request.user.id)
            form.save()
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('home')

@login_required(login_url='login')
def add_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        print(form.errors)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            etudiant = Etudiant.objects.create(nom_etudiant=cleaned_data['nom_etudiant'], post_nom=cleaned_data['post_nom'], prenom=cleaned_data['prenom'], date_naissance=cleaned_data['date_naissance'], matricule=cleaned_data['matricule'], password=cleaned_data['password'], login=cleaned_data['login'])
            Etude.objects.create(promotion=cleaned_data['promotion'], palmares=Palmares.objects.get(pk=cleaned_data['palmares']), etudiant=etudiant, valide=True)
            # palmares = form.save(commit=False)
            # palmares.universite = Universite.objects.get(pk=request.user.id)
            # form.save()
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('home')