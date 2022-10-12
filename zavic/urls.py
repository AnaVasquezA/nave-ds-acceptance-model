from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('submitAnswers', views.submit, name='submitAnswers'),
    path('check', views.check_results, name="check"),
    path('getResults', views.get_results, name="getResults"),
]
