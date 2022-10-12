from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('sendvars', views.send_variables, name='sendvars'),
    path('checkacc', views.check_acc, name='checkacc'),
    path('getAcceptance', views.get_acceptance, name='getAcceptance')
]
