import logging
import json
from django.core.mail import send_mail
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
    del dict['customer_rfc']
    rfc = request.POST.get('customer_rfc').upper()
    answer = Answer()
    answer.customer_rfc = rfc
    answer.answers = json.dumps(dict)
    answer.save()
    # logger.info(dict)
    m = int(dict['1a'])+int(dict['2d'])+int(dict['3a'])+int(dict['4b'])+int(dict['5b'])+int(dict['6b'])+int(dict['7a'])+int(dict['8d'])+int(dict['9d'])+int(dict['10a'])
    l = int(dict['1d'])+int(dict['2c'])+int(dict['3b'])+int(dict['4a'])+int(dict['5a'])+int(dict['6d'])+int(dict['7b'])+int(dict['8c'])+int(dict['9b'])+int(dict['10d'])
    i = int(dict['1b'])+int(dict['2a'])+int(dict['3d'])+int(dict['4c'])+int(dict['5d'])+int(dict['6a'])+int(dict['7c'])+int(dict['8b'])+int(dict['9a'])+int(dict['10b'])
    c = int(dict['1c'])+int(dict['2b'])+int(dict['3c'])+int(dict['4d'])+int(dict['5c'])+int(dict['6c'])+int(dict['7d'])+int(dict['8a'])+int(dict['9c'])+int(dict['10c'])

    if(c >= 28 and (m <= 26 or l <= 26 or i >= 28)):
        result = 'RECHAZADO'
    elif (c >= 14 and c <= 26):
        result = 'ACEPTADO CON REVISIÓN'
    else:
        result = 'ACEPTADO'

    answer.result = result
    answer.save()

    send_mail('Resultados '+rfc, 'Moral='+str(m) +'\nLegal='+str(l)+'\nIndiferente='+str(i)+'\nCorrupto='+str(c)+'\nResultado='+result, 'ana.vasquez@nave.mx', ['sofia@nave.mx'], fail_silently=False)
    # logger.info(json.dumps(dict))
    return JsonResponse({"message": "Respuestas enviadas correctamente"})

def check_results(request):
    return render(request, 'check.html')

def get_results(request):
    context = {"answers": [4,3,2,1]}
    if (request.POST.get('customer_rfc') != ''):
        answer = Answer.objects.get(pk=request.POST.get('customer_rfc').upper())
        context["rfc"] = answer.customer_rfc
        context["results"] = json.loads(answer.answers)
        m = int(context["results"]["1a"])+int(context["results"]["2d"])+int(context["results"]["3a"])+int(context["results"]["4b"])+int(context["results"]["5b"])+int(context["results"]["6b"])+int(context["results"]["7a"])+int(context["results"]["8d"])+int(context["results"]["9d"])+int(context["results"]["10a"])
        l = int(context["results"]["1d"])+int(context["results"]["2c"])+int(context["results"]["3b"])+int(context["results"]["4a"])+int(context["results"]["5a"])+int(context["results"]["6d"])+int(context["results"]["7b"])+int(context["results"]["8c"])+int(context["results"]["9b"])+int(context["results"]["10d"])
        i = int(context["results"]["1b"])+int(context["results"]["2a"])+int(context["results"]["3d"])+int(context["results"]["4c"])+int(context["results"]["5d"])+int(context["results"]["6a"])+int(context["results"]["7c"])+int(context["results"]["8b"])+int(context["results"]["9a"])+int(context["results"]["10b"])
        c = int(context["results"]["1c"])+int(context["results"]["2b"])+int(context["results"]["3c"])+int(context["results"]["4d"])+int(context["results"]["5c"])+int(context["results"]["6c"])+int(context["results"]["7d"])+int(context["results"]["8a"])+int(context["results"]["9c"])+int(context["results"]["10c"])
        context["m"] = m
        context["l"] = l
        context["i"] = i
        context["c"] = c
        context["result"] = answer.result

        return render(request, 'results.html', context)
    else:
        return JsonResponse({"error": "RFC de usuario no encontrado o vacio"})
