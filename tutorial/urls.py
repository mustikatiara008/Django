from django.urls import path
from . import views

app_name = 'Contact'

urlpatterns = [

    path('list', views.KontakView, name='kontakList'),

]
