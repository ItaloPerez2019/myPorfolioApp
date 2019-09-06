from django.urls import path
from . import views

urlpatterns = [

    path('',views.appones, name = 'appone'),
    path('count/',views.count, name = 'count'),

]
