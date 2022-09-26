import uuid
from django.db import models

class EduLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class MaritalStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class INECoin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class HousingTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class HouseMates(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class HousingType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class EcoDependents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class PrevOccupation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class PlatRegistTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class DrivingTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class TypeinPlataform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class Earnings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class AngerExp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, null=True)

class ViolenceCriteria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, null=True)

class LegalBack(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class OtherIncome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class LateResponse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class MonthlyExpenses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class Parking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class IncomeRise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class WorkingHours(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class WorkingHoursPrev(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class LastIncome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class IncomeExp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class Plataform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class LastDrive(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class DrivenCar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class PlatExit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class OppArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class LawsuitMatter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class AlcoholIntake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class ForeignTrips(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class DUI(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class PlatAccidents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class LastAccident(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class Questionnaire(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class AddressIne(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class Multiplataform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)

class ProfileVariables(models.Model):
    customer_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    age = models.IntegerField(null=True)
    edu_level = models.ForeignKey(EduLevel, on_delete=models.SET_NULL, null=True)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.SET_NULL, null=True)
    INE_coincidence = models.ForeignKey(INECoin, on_delete=models.SET_NULL, null=True)
    housing_time = models.ForeignKey(HousingTime, on_delete=models.SET_NULL, null=True)
    housing_mates = models.ForeignKey(HouseMates, on_delete=models.SET_NULL, null=True)
    housing_type = models.ForeignKey(HousingType, on_delete=models.SET_NULL, null=True)
    eco_dependents = models.ForeignKey(EcoDependents, on_delete=models.SET_NULL, null=True)
    prev_occupation = models.ForeignKey(PrevOccupation, on_delete=models.SET_NULL, null=True)
    other_source_income = models.ForeignKey(OtherIncome, on_delete=models.SET_NULL, null=True)
    registered_time = models.ForeignKey(PlatRegistTime, on_delete=models.SET_NULL, null=True)
    driving_time = models.ForeignKey(DrivingTime, on_delete=models.SET_NULL, null=True)
    plat_type = models.ForeignKey(TypeinPlataform, on_delete=models.SET_NULL, null=True)
    earnings = models.ForeignKey(Earnings, on_delete=models.SET_NULL, null=True)
    plat_score = models.FloatField(null=True)
    anger_exp = models.ForeignKey(AngerExp, on_delete=models.SET_NULL, null=True)
    vio_criteria = models.ForeignKey(ViolenceCriteria, on_delete=models.SET_NULL, null=True)
    legal_back = models.ForeignKey(LegalBack, on_delete=models.SET_NULL, null=True)
    anger_mgmt = models.IntegerField(null=True)
    default_tendency = models.IntegerField(null=True)
    strong_words = models.IntegerField(null=True)
    time_effort_inv = models.IntegerField(null=True)
    quick_anger = models.IntegerField(null=True)
    keeping_objs = models.IntegerField(null=True)
    steal_tendency = models.IntegerField(null=True)
    get_job_done = models.IntegerField(null=True)
    unconcerned = models.IntegerField(null=True)
    unthink_tendency = models.IntegerField(null=True)
    lie_tendency = models.IntegerField(null=True)
    disregard_tendency = models.IntegerField(null=True)
    enjoys_adrenaline = models.IntegerField(null=True)
    enjoys_fast_driving = models.IntegerField(null=True)
    drives_fast = models.IntegerField(null=True)
    took_time_respond = models.ForeignKey(LateResponse, on_delete=models.SET_NULL, null=True)
    stable_profile = models.IntegerField(null=True)
    pasive_agresive_profile = models.IntegerField(null=True)
    impulsive_profile = models.IntegerField(null=True)
    result = models.CharField(max_length=50, null=True)
    cat_activo = models.DecimalField(max_digits=11, decimal_places=8, null=True)
    cat_devo =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    cat_repo =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    cat_robos =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    oc_no =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    oc_si =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    ts_asalto =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    ts_choque =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    ts_otro =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    ts_percance =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    ts_robo =  models.DecimalField(max_digits=11, decimal_places=8, null=True)
    name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    address_ine = models.ForeignKey(AddressIne, on_delete=models.SET_NULL, null=True)
    monthly_expenses = models.ForeignKey(MonthlyExpenses, on_delete=models.SET_NULL, null=True)
    parking = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True)
    address_other = models.CharField(max_length=500, null=True)
    income_rise = models.ForeignKey(IncomeRise, on_delete=models.SET_NULL, null=True)
    tax_stamps = models.BooleanField(null=True)
    tax_stamps_loaded = models.BooleanField(null=True)
    working_hours_prev = models.ForeignKey(WorkingHoursPrev, on_delete=models.SET_NULL, null=True)
    last_income = models.ForeignKey(LastIncome, on_delete=models.SET_NULL, null=True)
    working_hours = models.ForeignKey(WorkingHours, on_delete=models.SET_NULL, null=True)
    income_expectations = models.ForeignKey(IncomeExp, on_delete=models.SET_NULL, null=True)
    plataform = models.ForeignKey(Plataform, on_delete=models.SET_NULL, null=True)
    plat_score_motive = models.CharField(max_length=200, null=True)
    trips = models.IntegerField(null=True)
    multiplataform = models.ForeignKey(Multiplataform, on_delete=models.SET_NULL, null=True)
    multiplat_score = models.FloatField(null=True)
    multiplat_score_motive = models.CharField(max_length=200, null=True)
    multiplat_trips = models.IntegerField(null=True)
    last_drive = models.ForeignKey(LastDrive, on_delete=models.SET_NULL, null=True)
    driven_car_type = models.ForeignKey(DrivenCar, on_delete=models.SET_NULL, null=True)
    plat_exit_motive = models.ForeignKey(PlatExit, on_delete=models.SET_NULL, null=True)
    car_workshop_motive = models.CharField(max_length=500, null=True)
    carjacking_zone =  models.CharField(max_length=200, null=True)
    re_entry = models.BooleanField(null=True)
    opp_area = models.ForeignKey(OppArea, on_delete=models.SET_NULL, null=True)
    cc_mgmt = models.BooleanField(null=True)
    lawsuit_matter = models.ForeignKey(LawsuitMatter, on_delete=models.SET_NULL, null=True)
    states = models.CharField(max_length=500, null=True)
    alcohol_intake = models.ForeignKey(AlcoholIntake, on_delete=models.SET_NULL, null=True)
    foreign_trips = models.ForeignKey(ForeignTrips, on_delete=models.SET_NULL, null=True)
    dui = models.ForeignKey(DUI, on_delete=models.SET_NULL, null=True)
    freq_states = models.CharField(max_length=500, null=True)
    plat_accidents = models.ForeignKey(PlatAccidents, on_delete=models.SET_NULL, null=True)
    plat_acc_motive = models.CharField(max_length=500, null=True)
    last_accident = models.ForeignKey(LastAccident, on_delete=models.SET_NULL, null=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, null=True)
    risk_before_accu = models.CharField(max_length=2000, null=True)
