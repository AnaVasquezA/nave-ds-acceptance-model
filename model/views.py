import logging
import pickle
import pandas as pd
import csv
import os
from django.shortcuts import redirect
from django.conf import settings
from django_pandas.io import read_frame
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import EduLevel, MaritalStatus, INECoin, TypeinPlataform, Earnings, AngerExp, ViolenceCriteria, LegalBack, ProfileVariables, HousingTime, HouseMates, HousingType, EcoDependents, PrevOccupation, PlatRegistTime, DrivingTime
from django.forms.models import model_to_dict
from pathlib import Path

HERE = Path(__file__).parent

logger = logging.getLogger('django')

def home(request):
    return render(request, 'home.html')

def check_acc(request):
    return render(request, 'check_acc.html')

def register(request):
    data = {
    "education": EduLevel.objects.all(),
    "marital": MaritalStatus.objects.all(),
    "ine": INECoin.objects.all(),
    "h_time": HousingTime.objects.all(),
    "h_mates": HouseMates.objects.all(),
    "h_type": HousingType.objects.all(),
    "eco_de": EcoDependents.objects.all(),
    "o_prev": PrevOccupation.objects.all(),
    "plattime": PlatRegistTime.objects.all(),
    "d_time": DrivingTime.objects.all(),
    "plattype": TypeinPlataform.objects.all(),
    "earns": Earnings.objects.all(),
    "aexp":AngerExp.objects.all(),
    "violence":ViolenceCriteria.objects.all(),
    "legal": LegalBack.objects.all()
    }
    return render(request, 'register.html', data)

def send_variables(request):
    logger.info(request.POST.get('edu_level'))
    profile = ProfileVariables()
    profile.customer_id = request.POST.get('customer_id')
    profile.age = request.POST.get('age')
    profile.edu_level_id = request.POST.get('edu_level')
    profile.marital_status_id = request.POST.get('marital')
    profile.INE_coincidence_id = request.POST.get('ine')
    profile.housing_time_id = request.POST.get('housing_time')
    profile.housing_mates_id = request.POST.get('housing_mates')
    profile.housing_type_id = request.POST.get('housing_type')
    profile.eco_dependents_id = request.POST.get('eco_dependents')
    profile.prev_occupation_id = request.POST.get('prev_occupation')
    profile.other_source_income_id = request.POST.get('other_income')
    profile.registered_time_id = request.POST.get('registered_time')
    profile.driving_time_id = request.POST.get('driving_time')
    profile.plat_type_id = request.POST.get('plat_type')
    profile.earnings_id = request.POST.get('earnings')
    profile.plat_score = request.POST.get('plat_score')
    profile.anger_exp_id = request.POST.get('anger_exp')
    profile.vio_criteria_id = request.POST.get('vio_criteria')
    profile.legal_back_id = request.POST.get('legal_back')
    profile.anger_mgmt = request.POST.get('anger_mgmt')
    profile.default_tendency = request.POST.get('default_tendency')
    profile.strong_words = request.POST.get('strong_words')
    profile.time_effort_inv = request.POST.get('time_effort_inv')
    profile.quick_anger = request.POST.get('quick_anger')
    profile.keeping_objs = request.POST.get('keeping_objs')
    profile.steal_tendency = request.POST.get('steal_tendency')
    profile.get_job_done = request.POST.get('get_job_done')
    profile.unconcerned = request.POST.get('unconcerned')
    profile.unthink_tendency = request.POST.get('unthink_tendency')
    profile.lie_tendency = request.POST.get('lie_tendency')
    profile.disregard_tendency = request.POST.get('disregard_tendency')
    profile.enjoys_adrenaline = request.POST.get('enjoys_adrenaline')
    profile.enjoys_fast_driving = request.POST.get('enjoys_fast_driving')
    profile.drives_fast = request.POST.get('drives_fast')
    profile.took_time_respond_id = request.POST.get('late_response')
    profile.stable_profile = request.POST.get('stable_profile')
    profile.pasive_agresive_profile = request.POST.get('pasive_agresive_profile')
    profile.impulsive_profile = request.POST.get('impulsive_profile')
    profile.save()

    with open(HERE / 'modelo_aprobado_denegado.pkl', 'rb') as f:
        model = pickle.load(f)
    # logger.info(model_to_dict(profile))
    model = pickle.load(open(HERE /'modelo_aprobado_denegado.pkl', 'rb'))
    file_name = os.path.join(settings.MEDIA_ROOT, "driver.csv")
    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['Edad', 'Educación', 'Estado Civil',
           'Coincidencia INE-Comprobante', 'Tiempo en vivienda',
           'Con quién vive', 'Tipo de vivienda', 'Dependientes Ecónomicos',
           'Ocupación anterior', 'Otra fuente ingresos',
           'Tiempo registrado en plataforma',
           'Tiempo conduciendo continuo', 'Alta en plataforma',
           'A quien le depositaban ganancias', 'Calificacion Plataforma',
           'Expresión del enojo', 'Criterio Violencia',
           'Antecedentes legales o penales',
           'Control del enojo', 'Tendencia a incumplir', 'Uso de palabras fuertes',
           'Inversión de tiempo y esfuerzo', 'Enojo fácil',
           'Quedarse objetos ajenos', 'Tendencia a robo',
           'Sacar adelante el trabajo', 'Se considera despreocupado',
           'Tendencia a actuar sin pensar', 'Tendencia a mentir',
           'Tendencia a no hacer caso', 'Disfruta la adrenalina',
           'Gusto por manejar a velocidad', 'Manejar a velocidad',
           'Tardó en dar respuestas', 'Perfil estable', 'Perfil pasivo-agresivo',
           'Perfil impulsivo'])
        writer.writerow([profile.age, profile.edu_level_id, profile.marital_status_id, profile.INE_coincidence_id, profile.housing_time_id, profile.housing_mates_id, profile.housing_type_id, profile.eco_dependents_id, profile.prev_occupation_id, profile.other_source_income_id, profile.registered_time_id, profile.driving_time_id, profile.plat_type_id, profile.earnings_id, profile.plat_score, profile.anger_exp_id, profile.vio_criteria_id, profile.legal_back_id, profile.anger_mgmt, profile.default_tendency, profile.strong_words, profile.time_effort_inv, profile.quick_anger, profile.keeping_objs, profile.steal_tendency, profile.get_job_done, profile.unconcerned, profile.unthink_tendency, profile.lie_tendency, profile.disregard_tendency, profile.enjoys_adrenaline, profile.enjoys_fast_driving, profile.drives_fast, profile.took_time_respond_id, profile.stable_profile, profile.pasive_agresive_profile, profile.impulsive_profile])
    df = pd.read_csv('driver.csv')
    result = model.predict(df)

    return JsonResponse({"Resultado": result[0]})

def getAcceptance(request):
    data = {
    "education": EduLevel.objects.all(),
    "marital": MaritalStatus.objects.all(),
    "ine": INECoin.objects.all(),
    "h_time": HousingTime.objects.all(),
    "h_mates": HouseMates.objects.all(),
    "h_type": HousingType.objects.all(),
    "eco_de": EcoDependents.objects.all(),
    "o_prev": PrevOccupation.objects.all(),
    "plattime": PlatRegistTime.objects.all(),
    "d_time": DrivingTime.objects.all(),
    "plattype": TypeinPlataform.objects.all(),
    "earns": Earnings.objects.all(),
    "aexp":AngerExp.objects.all(),
    "violence":ViolenceCriteria.objects.all(),
    "legal": LegalBack.objects.all()
    }
    if (request.POST.get('customer_id') != ''):
        profile = ProfileVariables.objects.get(pk=request.POST.get('customer_id'))
        data["profile"] = profile
        # logger.info(profile)
        with open(HERE / 'modelo_aprobado_denegado.pkl', 'rb') as f:
            model = pickle.load(f)
        # logger.info(model_to_dict(profile))
        model = pickle.load(open(HERE /'modelo_aprobado_denegado.pkl', 'rb'))
        file_name = os.path.join(settings.MEDIA_ROOT, "driver.csv")
        with open(file_name, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(['Edad', 'Educación', 'Estado Civil',
               'Coincidencia INE-Comprobante', 'Tiempo en vivienda',
               'Con quién vive', 'Tipo de vivienda', 'Dependientes Ecónomicos',
               'Ocupación anterior', 'Otra fuente ingresos',
               'Tiempo registrado en plataforma',
               'Tiempo conduciendo continuo', 'Alta en plataforma',
               'A quien le depositaban ganancias', 'Calificacion Plataforma',
               'Expresión del enojo', 'Criterio Violencia',
               'Antecedentes legales o penales',
               'Control del enojo', 'Tendencia a incumplir', 'Uso de palabras fuertes',
               'Inversión de tiempo y esfuerzo', 'Enojo fácil',
               'Quedarse objetos ajenos', 'Tendencia a robo',
               'Sacar adelante el trabajo', 'Se considera despreocupado',
               'Tendencia a actuar sin pensar', 'Tendencia a mentir',
               'Tendencia a no hacer caso', 'Disfruta la adrenalina',
               'Gusto por manejar a velocidad', 'Manejar a velocidad',
               'Tardó en dar respuestas', 'Perfil estable', 'Perfil pasivo-agresivo',
               'Perfil impulsivo'])
            writer.writerow([profile.age, profile.edu_level_id, profile.marital_status_id, profile.INE_coincidence_id, profile.housing_time_id, profile.housing_mates_id, profile.housing_type_id, profile.eco_dependents_id, profile.prev_occupation_id, profile.other_source_income_id, profile.registered_time_id, profile.driving_time_id, profile.plat_type_id, profile.earnings_id, profile.plat_score, profile.anger_exp_id, profile.vio_criteria_id, profile.legal_back_id, profile.anger_mgmt, profile.default_tendency, profile.strong_words, profile.time_effort_inv, profile.quick_anger, profile.keeping_objs, profile.steal_tendency, profile.get_job_done, profile.unconcerned, profile.unthink_tendency, profile.lie_tendency, profile.disregard_tendency, profile.enjoys_adrenaline, profile.enjoys_fast_driving, profile.drives_fast, profile.took_time_respond_id, profile.stable_profile, profile.pasive_agresive_profile, profile.impulsive_profile])
        df = pd.read_csv('driver.csv')
        result = model.predict(df)
        data["result"] = result
        logger.info(result)
        return render(request, 'acceptance.html', data)
    else:
        return JsonResponse({"error": "Id de usuario no encontrado o vacio"})
