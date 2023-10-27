from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Etudiant, Palmares, Universite, Etude, Parcous

from .forms import PalmaresForm, EtudiantForm

# Create your views here.
def home(request):
    universites = Universite.objects.all()
    return render(request, 'transfertApp/home.html', {'universites': universites})

def voir_palmares(request):
    universites = Universite.objects.all()
    return render(request, 'transfertApp/trouverPalmares.html', {'universites': universites})

def demande_inscription(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        etude = Etude.objects.filter(palmares_id=form['source'])
        etudiant = Etudiant.objects.filter(login=form['login'], password=form['password'], etude__in=etude)
        if (etudiant):
            etude_dest = Etude.objects.create(palmares=Palmares.objects.get(pk=form['destination']), etudiant=etudiant[0], promotion=form['promotion'])
            return redirect('demander-inscription')
        else:
            palmares = Palmares.objects.all()
            return render(request, 'transfertApp/demandeInscription.html', {'palmares': palmares, 'no_passed': True})
        
    else:
        palmares = Palmares.objects.all()
        return render(request, 'transfertApp/demandeInscription.html', {'palmares': palmares})


@login_required(login_url='login')
def dashboard(request):
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
        form = PalmaresForm(request.POST, request.FILES)
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
            palm = Palmares.objects.get(pk=cleaned_data['palmares'])
            Etude.objects.create(promotion=cleaned_data['promotion'], palmares=palm, etudiant=etudiant, valide=True)
            Parcous.objects.create(anne_acad=palm.annee, promotion=cleaned_data['promotion'], etudiant=etudiant)
            # palmares = form.save(commit=False)
            # palmares.universite = Universite.objects.get(pk=request.user.id)
            # form.save()
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('home')

@login_required
def profile_invalid(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    return render(request, "transfertApp/invalidatedProfile.html", {"profile": etudiant})

def valider_etudiant(request, id):
    etude = Etude.objects.get(etudiant=Etudiant.objects.get(pk=id))
    etude.valide = True
    etude.save()
    return redirect('home')