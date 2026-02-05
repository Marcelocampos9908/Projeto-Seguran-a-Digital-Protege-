from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('registar/', views.registar, name='registar'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
    path('home2/', views.home2, name='home2'),
    path('quiz/', views.quiz, name='quiz'),
    path('proximo_passo/', views.proximo_passo, name='proximo_passo'),
    path('quiz_final/', views.quiz_final, name='quiz_final'),
    path('simulador/', views.simulador, name='simulador'),
    path('proximo_email/', views.proximo_email, name='proximo_email'),
]