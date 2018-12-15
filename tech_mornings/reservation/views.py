from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Reservation
from django.views.generic import ListView
from django.views.generic.edit import CreateView


def index (request):
    """
    this method alows to create a shorting by list from clients
    and use render object to present into view.
    :param request: request.
    :return: render object instance.
    """
    clients_list = Client.objects.order_by('-create_date')
    context = {
        'clients_list': clients_list
    }
    return render(request, 'reservation/index.html',context)

class ReservationCreate(CreateView):
    """
    this class allows to create reservation view.
    """
    model = Reservation
    success_url = '/reservation/list'
    fields = '__all__'

class ReservationList(ListView):
    """
    this class allows to create reservation list view.
    """
    model = Reservation

