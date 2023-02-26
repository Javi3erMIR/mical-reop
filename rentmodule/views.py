from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
# from azure.core.credentials import AzureKeyCredential
# from azure.ai.textanalytics import TextAnalyticsClient
from .models import *
from .forms import *

def home (request):
    return render(request,'home.html',{})

@csrf_exempt
@login_required
def reservas(request):
    username = request.user.username

    reservas = Reserva.objects.all()
    autos = Car.objects.all()

    context = {
        'reservas': reservas,
        'autos': autos,
        'username': username,
    }
    return render(request, 'reservas.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def crear_reserva(request):
    autos = Car.objects.all()

    context = {
        'autos': autos
    }

    com = request.POST.get('comentarios')
    car_model = str(request.POST.get('selautos'))
    username = request.user.username

    Reserva(car_model=car_model, comentarios=com, user_name=username).save()
    render(request, 'reservas.html', context)

    return redirect(reverse('reservas'))

def get_reserva(request):
    
    reservas = Reserva.objects.all()
    autos = Car.objects.all()

    context = {
        'reservas': reservas,
        'autos': autos
    }

    return render(request, 'reservas.html', context)

@csrf_exempt
def edit(request):    
    car_model=request.POST.get('car_model')
    print(car_model)
    new_car_model = request.POST.get('selautos')
    com = request.POST.get('comentarios')

    reserva = Reserva.objects.get(car_model=car_model)
    reserva.car_model = new_car_model
    reserva.comentarios = com


    reserva.save()
    return redirect(reverse('reservas'))
    


@csrf_exempt
def eliminar_reserva(request):
    try:
        car_model=request.POST.get('car_model')
        reservas = Reserva.objects.filter(car_model=car_model)

        for reserva in reservas:
            reserva.delete()

        return HttpResponse(status=204)
    except Exception as e:
        print(e)


# def crear_auto(request):
#     Car(car_brand='Ford', car_model='Focus', car_color='Azul').save()
#     Car(car_brand='Chevrolet', car_model='Cavalier', car_color='Gris').save()
#     Car(car_brand='Honda', car_model='Civic', car_color='Negro').save()
#     Car(car_brand='Toyota', car_model='Corolla', car_color='Blanco').save()

#     return HttpResponse({"status": 200, "msg": 'ok'})
