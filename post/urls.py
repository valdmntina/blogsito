from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="posts"),
    path('storage/<str:titulo>/<str:cuerpo>/', views.storage, name="storage"),
    path('consultar/<int:id>', views.mostrar_id, name='consultar'),
    path('modificar/<str:titulo>/<int:id>', views.modificar, name='consultar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('consultas/', views.consultas, name='consultas')
]