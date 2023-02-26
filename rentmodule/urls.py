from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('reservas/', views.reservas, name='reservas'),
    path('logout/', views.logout_view, name='logout'),
    path('crear-reserva/', views.crear_reserva, name='crear_reserva'),
    path('get-reserva/', views.get_reserva, name='get-reserva'),
    path('eliminar-reserva', views.eliminar_reserva, name='eliminar-reserva'),
    path('edit/', views.edit, name='edit')
    # path('autos/', views.crear_auto)
]
