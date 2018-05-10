from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPacientes.as_view()),
    path('<int:pk>/', views.DetailPaciente.as_view()),
]