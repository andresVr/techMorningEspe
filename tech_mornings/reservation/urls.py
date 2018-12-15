from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'), # this path is not a class because you need to define a single code for sorting results
    path('new/', views.ReservationCreate.as_view() , name ='reservation-add'), # this path is created based on create view django tool
    path('list/', views.ReservationList.as_view() , name ='reservation-view') # this path is created based on list view django tool

]