from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Reservation
from django.views.generic import ListView
from django.views.generic.edit import CreateView

def index (request):
    clients_list = Client.objects.order_by('-create_date')
    context = {
        'clients_list': clients_list
    }
    return render(request, 'reservation/index.html',context)

class ReservationCreate(CreateView):
    model = Reservation
    success_url = '/reservation/list'
    fields = '__all__'

class ReservationList(ListView):
    model = Reservation

