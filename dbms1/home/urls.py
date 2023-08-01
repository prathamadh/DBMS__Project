from django.urls import path 
from . import views



urlpatterns = [
    path('',views.index,name="index"),
    path('hello/',views.hello_view,name="hello"),
    path('pescriptionhistory/',views.p_history,name="p_history"),
    path('appointment/',views.appointment,name="appointment"),



]
