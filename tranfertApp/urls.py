from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', auth_views.LoginView.as_view(), {'next_page': '/dashboard'}, name='login'),
    path('log_out', auth_views.LogoutView.as_view(), {'next_page': '/login'}, name='logout'),
    path('student-validated', views.validated_etudiants, name='validated-student'),
    path('student-invalidated', views.invalidated_etudiants, name='invalidated-student'),
    path('add-palmares', views.add_palmares, name="add-palmares"),
    path('add-etudiant', views.add_etudiant, name="add-etudiant"),
    path('invalid-profile/<int:id>', views.profile_invalid, name="profile-invalid"),
    path('valid-profile/<int:id>', views.profile_valid, name="profile-valid"),
    path('validate-etudiant/<int:id>', views.valider_etudiant, name="validate-etudiant"),
    path('add-parcours/<int:id>', views.add_parcours, name="add-parcours"),
    path('demander-inscription/<int:id_palmares>', views.demande_inscription, name='demander-inscription'),
    path('voir-palmares', views.voir_palmares, name="voir-palmares"),
    path('search/', views.search_palmares, name="search-palmares")
]
