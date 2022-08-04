import logging
import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer
from django.http import JsonResponse

logger = logging.getLogger('django')

def index(request):
    return render(request, 'index.html')

def test(request):
    context = {"answers": [4,3,2,1]}
    return render(request, 'test.html', context)

def submit(request):
    dict = request.POST.copy()
    del dict['csrfmiddlewaretoken']
    del dict['customer_id']
    answer = Answer()
    answer.customer_id = request.POST.get('customer_id')
    answer.answers = json.dumps(dict)
    answer.save()
    # quitar el token "csrfmiddlewaretoken" de la respuesta
    # logger.info(json.dumps(dict))
    return JsonResponse({"mesaage": "Respuestas enviadas correctamente"})

def check_results(request):
    return render(request, 'check.html')

def get_results(request):
    context = {"answers": [4,3,2,1]}
    if (request.POST.get('customer_id') != ''):
        answer = Answer.objects.get(pk=request.POST.get('customer_id'))
        context["results"] = json.loads(answer.answers)
        context["m"] = int(context["results"]["1a"])+int(context["results"]["2d"])+int(context["results"]["3a"])+int(context["results"]["4b"])+int(context["results"]["5b"])+int(context["results"]["6b"])+int(context["results"]["7a"])+int(context["results"]["8d"])+int(context["results"]["9d"])+int(context["results"]["10a"])
        context["l"] = int(context["results"]["1d"])+int(context["results"]["2c"])+int(context["results"]["3b"])+int(context["results"]["4a"])+int(context["results"]["5a"])+int(context["results"]["6d"])+int(context["results"]["7b"])+int(context["results"]["8c"])+int(context["results"]["9b"])+int(context["results"]["10d"])
        context["i"] = int(context["results"]["1b"])+int(context["results"]["2a"])+int(context["results"]["3d"])+int(context["results"]["4c"])+int(context["results"]["5d"])+int(context["results"]["6a"])+int(context["results"]["7c"])+int(context["results"]["8b"])+int(context["results"]["9a"])+int(context["results"]["10b"])
        context["c"] = int(context["results"]["1c"])+int(context["results"]["2b"])+int(context["results"]["3c"])+int(context["results"]["4d"])+int(context["results"]["5c"])+int(context["results"]["6c"])+int(context["results"]["7d"])+int(context["results"]["8a"])+int(context["results"]["9c"])+int(context["results"]["10c"])
        return render(request, 'results.html', context)
    else:
        return JsonResponse({"error": "Id de usuario no encontrado o vacio"})
