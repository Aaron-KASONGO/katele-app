from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .models import Etudiant, Palmares, Universite, Etude, Parcous

from .forms import PalmaresForm, EtudiantForm, Parcoursform


EMAIL_CONTENT_STUDENT = """
Votre demande d'inscription a été enregistrée avec succès
"""
EMAIL_CONTENT_UNIV = """
Un étudiant a fait une demande d'inscription à votre université
"""
EMAIL_CONTENT_STUDENT_VALIDATED = """
Votre demande d'inscription a été validé !
"""

# Create your views here.
def home(request):
    universites = Universite.objects.all()
    return render(request, 'transfertApp/home.html', {'universites': universites})

def voir_palmares(request):
    universites = Universite.objects.all()
    return render(request, 'transfertApp/trouverPalmares.html', {'universites': universites})

def demande_inscription(request, id_palmares=None):
    if request.method == 'POST':
        form = request.POST
        print(form)
        etude = Etude.objects.filter(palmares_id=form['source'])
        etudiant = Etudiant.objects.filter(login=form['login'], password=form['password'], etude__in=etude)
        if (etudiant):
            etude_dest = Etude.objects.create(palmares=Palmares.objects.get(pk=form['destination']), etudiant=etudiant[0], promotion=form['promotion'])
            # send_mail(
            #     "Demande d'inscription",
            #     EMAIL_CONTENT_STUDENT,
            #     settings.EMAIL_HOST_USER,
            #     [etudiant[0].login],
            #     fail_silently=False
            # )
            return redirect('dashboard')
        else:
            palmares = Palmares.objects.exclude(pk=id_palmares)
            single_palm = Palmares.objects.get(pk=id_palmares)
            return render(request, 'transfertApp/demandeInscription.html', {'palmares': palmares, 'no_passed': True, 'single_palm': single_palm})
        
    else:
        palmares = Palmares.objects.exclude(pk=id_palmares)
        single_palm = Palmares.objects.get(pk=id_palmares)
        return render(request, 'transfertApp/demandeInscription.html', {'palmares': palmares, 'single_palm': single_palm})


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
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return redirect('dashboard')

@login_required(login_url='login')
def add_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        # form_file = Parcoursform(request.POST, request.FILES)
        # print(form_file.errors)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            etudiant = Etudiant.objects.create(nom_etudiant=cleaned_data['nom_etudiant'], post_nom=cleaned_data['post_nom'], prenom=cleaned_data['prenom'], date_naissance=cleaned_data['date_naissance'], matricule=cleaned_data['matricule'], password=cleaned_data['password'], login=cleaned_data['login'])
            palm = Palmares.objects.get(pk=cleaned_data['palmares'])
            Etude.objects.create(promotion=cleaned_data['promotion'], palmares=palm, etudiant=etudiant, valide=True)
            # palmares = form.save(commit=False)
            # palmares.universite = Universite.objects.get(pk=request.user.id)
            # form.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return redirect('dashboard')

@login_required(login_url='login')
def profile_invalid(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    return render(request, "transfertApp/invalidatedProfile.html", {"profile": etudiant})

@login_required(login_url='login')
def profile_valid(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    return render(request, "transfertApp/validatedProfile.html", {"profile": etudiant})

@login_required(login_url='login')
def valider_etudiant(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    etude = Etude.objects.get(etudiant=etudiant, valide=False)
    etude.valide = True
    etude.save()
    # send_mail(
    #     "Demande d'inscription",
    #     EMAIL_CONTENT_STUDENT_VALIDATED,
    #     settings.EMAIL_HOST_USER,
    #     [etudiant.login],
    #     fail_silently=False
    # )
    return redirect('dashboard')

@login_required(login_url='login')
def add_parcours(request, id):
    if request.method == 'POST':
        form = Parcoursform(request.POST, request.FILES)
        # form_file = Parcoursform(request.POST, request.FILES)
        # print(form_file.errors)
        if form.is_valid():
            # palmares = form.save(commit=False)
            # palmares.universite = Universite.objects.get(pk=request.user.id)
            # form.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return redirect('dashboard')