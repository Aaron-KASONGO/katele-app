from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('log_out', auth_views.LogoutView.as_view(), {'next_page': '/dashboard'}, name='logout'),
    path('student-validated', views.validated_etudiants, name='validated-student'),
    path('student-invalidated', views.invalidated_etudiants, name='invalidated-student'),
    path('add-palmares', views.add_palmares, name="add-palmares"),
    path('add-etudiant', views.add_etudiant, name="add-etudiant"),
    path('invalid-profile/<int:id>', views.profile_invalid, name="profile-invalid"),
    path('validate-etudiant/<int:id>', views.valider_etudiant, name="validate-etudiant"),
    path('demander-inscription', views.demande_inscription, name='demander-inscription'),
    path('voir-palmares', views.voir_palmares, name="voir-palmares")
]
