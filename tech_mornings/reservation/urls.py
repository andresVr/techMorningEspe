from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('new/', views.ReservationCreate.as_view() , name ='reservation-add'),
    path('list/', views.ReservationList.as_view() , name ='reservation-view')

]