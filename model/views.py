import logging
import pickle
import pandas as pd
import csv
import os
import json
from django.conf import settings
from django_pandas.io import read_frame
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import EduLevel, MaritalStatus, INECoin, TypeinPlataform, Earnings, AngerExp, ViolenceCriteria, LegalBack, ProfileVariables, HousingTime, HouseMates, HousingType, EcoDependents, PrevOccupation, PlatRegistTime, DrivingTime, MonthlyExpenses, Parking, WorkingHours, WorkingHoursPrev, LastIncome, IncomeExp, Plataform, LastDrive, DrivenCar, PlatExit, OppArea, LawsuitMatter, AlcoholIntake, DUI, PlatAccidents, LastAccident, Questionnaire, IncomeRise, ForeignTrips, AddressIne, Multiplataform
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
    "legal": LegalBack.objects.all(),
    "expenses": MonthlyExpenses.objects.all(),
    "parking": Parking.objects.all(),
    "rise": IncomeRise.objects.all(),
    "w_hours": WorkingHours.objects.all(),
    "w_hours_p": WorkingHoursPrev.objects.all(),
    "last_income": LastIncome.objects.all(),
    "incomeexp": IncomeExp.objects.all(),
    "plataforms": Plataform.objects.all(),
    "lastdrive": LastDrive.objects.all(),
    "drivencar": DrivenCar.objects.all(),
    "plat_exit": PlatExit.objects.all(),
    "opp_area": OppArea.objects.all(),
    "lawsuits": LawsuitMatter.objects.all(),
    "alcohol": AlcoholIntake.objects.all(),
    "dui": DUI.objects.all(),
    "foreigntrips": ForeignTrips.objects.all(),
    "plat_acc": PlatAccidents.objects.all(),
    "last_acc": LastAccident.objects.all(),
    "questionnaire": Questionnaire.objects.all(),
    "address_ine": AddressIne.objects.all(),
    "multiplataforms": Multiplataform.objects.all()
    }
    return render(request, 'register.html', data)

def send_variables(request):
    # logger.info(request.POST.get('edu_level'))
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
    profile.name = request.POST.get('name')
    profile.phone_number = request.POST.get('phone')
    profile.address_ine_id = request.POST.get('address_ine')
    profile.monthly_expenses_id =  request.POST.get('expenses')
    profile.parking_id = request.POST.get('parking')
    profile.address_other = request.POST.get('address_other')
    profile.income_rise_id = request.POST.get('income_rise')
    profile.tax_stamps = request.POST.get('tax_stamps')
    profile.tax_stamps_loaded = request.POST.get('tax_stamps_loaded')
    profile.working_hours_prev_id = request.POST.get('w_hours_prev')
    profile.last_income_id = request.POST.get('last_income')
    profile.working_hours_id = request.POST.get('w_hours')
    profile.income_expectations_id = request.POST.get('income_exp')
    profile.plataform_id = request.POST.get('plataform')
    profile.plat_score_motive = request.POST.get('plat_score_motive')
    profile.multiplat_trips = request.POST.get('multiplat_trips')
    profile.last_drive_id = request.POST.get('last_drive')
    profile.driven_car_type_id = request.POST.get('driven_car_type')
    profile.plat_exit_motive_id = request.POST.get('plat_exit_motive')
    profile.car_workshop_motive = request.POST.get('car_workshop_motive')
    profile.carjacking_zone = request.POST.get('carjacking_zone')
    profile.re_entry = request.POST.get('re_entry')
    profile.opp_area_id = request.POST.get('opp_area')
    profile.cc_mgmt = request.POST.get('cc_mgmt')
    profile.lawsuit_matter_id = request.POST.get('lawsuit_matter')
    profile.states = request.POST.get('states')
    profile.alcohol_intake_id = request.POST.get('alcohol_intake')
    profile.foreign_trips_id = request.POST.get('foreign_trips')
    profile.dui_id = request.POST.get('DUI')
    profile.freq_states = request.POST.get('freq_states')
    profile.plat_accidents_id = request.POST.get('plat_accidents')
    profile.plat_acc_motive = request.POST.get('plat_acc_motive')
    profile.last_accident_id = request.POST.get('last_accident')
    profile.questionnaire_id = request.POST.get('questionnaire')
    profile.risk_before_accu = request.POST.get('risk_before_accu')
    profile.trips = request.POST.get('trips')
    profile.multiplataform_id = request.POST.get('multiplataform')
    profile.multiplat_score = request.POST.get('multiplat_score')
    profile.multiplat_score_motive = request.POST.get('multiplat_score_motive')
    profile.save()

    model = pickle.load(open(HERE /'final_modelo_aprobado_denegado.pkl', 'rb'))
    transf = pd.read_pickle(HERE /'final_transf.pkl')
    categoria = pickle.load(open(HERE /'final_modelo_proba_categoria_stage.pkl', 'rb'))
    ocurrencia = pickle.load(open(HERE/'final_modelo_proba_ocurrencia_siniestro.pkl', 'rb'))
    tipo_siniestro = pickle.load(open(HERE /'final_modelo_tipo_siniestro.pkl', 'rb'))

    file_name = os.path.join(settings.MEDIA_ROOT, "driver.csv")
    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['edad', 'educacion', 'estado civil',
           'coincidencia ine comprobante', 'tiempo en vivienda',
           'con quien vive', 'tipo de vivienda', 'dependientes economicos',
           'ocupacion anterior', 'otra fuente ingresos',
           'tiempo registrado en plataforma',
           'tiempo conduciendo continuo', 'alta en plataforma',
           'a quien le depositaban ganancias', 'calificacion plataforma',
           'expresion del enojo', 'criterio violencia',
           'antecedentes legales o penales',
           'control del enojo', 'tendencia a incumplir', 'uso de palabras fuertes',
           'inversion de tiempo y esfuerzo', 'enojo facil',
           'quedarse objetos ajenos', 'tendencia a robo',
           'sacar adelante el trabajo', 'se considera despreocupado',
           'tendencia a actuar sin pensar', 'tendencia a mentir',
           'tendencia a no hacer caso', 'disfruta la adrenalina',
           'gusto por manejar a velocidad', 'manejar a velocidad',
           'tardo en dar respuestas', 'perfil estable', 'perfil pasivo agresivo',
           'perfil impulsivo'])
        writer.writerow([profile.age, profile.edu_level.value, profile.marital_status.value, profile.INE_coincidence.value, profile.housing_time.value, profile.housing_mates.value, profile.housing_type.value, profile.eco_dependents.value, profile.prev_occupation.value, profile.other_source_income.value, profile.registered_time.value, profile.driving_time.value, profile.plat_type.value, profile.earnings.value, profile.plat_score, profile.anger_exp.value, profile.vio_criteria.value, profile.legal_back.value, profile.anger_mgmt, profile.default_tendency, profile.strong_words, profile.time_effort_inv, profile.quick_anger, profile.keeping_objs, profile.steal_tendency, profile.get_job_done, profile.unconcerned, profile.unthink_tendency, profile.lie_tendency, profile.disregard_tendency, profile.enjoys_adrenaline, profile.enjoys_fast_driving, profile.drives_fast, profile.took_time_respond.value, profile.stable_profile, profile.pasive_agresive_profile, profile.impulsive_profile])

    df = pd.read_csv('driver.csv')
    categ = ['educacion', 'estado civil',
   'coincidencia ine comprobante', 'tiempo en vivienda',
   'con quien vive', 'tipo de vivienda', 'dependientes economicos',
   'ocupacion anterior', 'otra fuente ingresos',
   'tiempo registrado en plataforma',
   'tiempo conduciendo continuo', 'alta en plataforma',
   'a quien le depositaban ganancias', 'calificacion plataforma',
   'expresion del enojo', 'criterio violencia',
   'antecedentes legales o penales',
   'tardo en dar respuestas']
    df[categ] = df[categ].apply(transf.fit_transform)
    result = model.predict(df)

    profile.result = result[0]
    profile.save()

    cat = categoria.predict_proba(df)*100
    oc = ocurrencia.predict_proba(df)*100
    tipo = tipo_siniestro.predict_proba(df)*100

    profile.cat_activo = cat[0][0]
    profile.cat_devo = cat[0][1]
    profile.cat_repo = cat[0][2]
    profile.cat_robos = cat[0][3]
    profile.oc_no = oc[0][0]
    profile.oc_si = oc[0][1]
    profile.ts_asalto = tipo[0][0]
    profile.ts_choque = tipo[0][1]
    profile.ts_otro = tipo[0][2]
    profile.ts_percance = tipo[0][3]
    profile.ts_robo = tipo[0][4]
    profile.save()

    data = {
    "result": profile.result,
    "activo": profile.cat_activo,
    "devo": profile.cat_devo,
    "repo": profile.cat_repo,
    "robo": profile.cat_robos,
    "ocurrencia_no": profile.oc_no,
    "ocurrencia_si": profile.oc_si,
    "asalto": profile.ts_asalto,
    "choque": profile.ts_choque,
    "otro": profile.ts_otro,
    "percance": profile.ts_percance,
    "tipo_robo": profile.ts_robo
    }

    return render(request, 'acc_results.html', data)

def get_acceptance(request):
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
    "legal": LegalBack.objects.all(),
    "expenses": MonthlyExpenses.objects.all(),
    "parking": Parking.objects.all(),
    "rise": IncomeRise.objects.all(),
    "w_hours": WorkingHours.objects.all(),
    "w_hours_p": WorkingHoursPrev.objects.all(),
    "last_income": LastIncome.objects.all(),
    "incomeexp": IncomeExp.objects.all(),
    "plataforms": Plataform.objects.all(),
    "lastdrive": LastDrive.objects.all(),
    "drivencar": DrivenCar.objects.all(),
    "plat_exit": PlatExit.objects.all(),
    "opp_area": OppArea.objects.all(),
    "lawsuits": LawsuitMatter.objects.all(),
    "alcohol": AlcoholIntake.objects.all(),
    "dui": DUI.objects.all(),
    "foreigntrips": ForeignTrips.objects.all(),
    "plat_acc": PlatAccidents.objects.all(),
    "last_acc": LastAccident.objects.all(),
    "questionnaire": Questionnaire.objects.all(),
    "address_ine": AddressIne.objects.all(),
    "multiplataforms": Multiplataform.objects.all()
    }
    if (request.POST.get('customer_id') != ''):
        profile = ProfileVariables.objects.get(pk=request.POST.get('customer_id'))
        data["profile"] = profile
        return render(request, 'acceptance.html', data)
    else:
        return JsonResponse({"error": "Id de usuario no encontrado o vacio"})
