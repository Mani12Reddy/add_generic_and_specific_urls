from django.urls import path
from app1.views import *
app_name='aa'

urlpatterns=[

    path('mani/',mani,name='mani'),
    path('raju/',raju,name='raju'),
]
