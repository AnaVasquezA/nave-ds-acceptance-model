import uuid
from django.db import models

class EduLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class MaritalStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class INECoin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class HousingTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class HouseMates(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class HousingType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class EcoDependents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class PrevOccupation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class PlatRegistTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class DrivingTime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class TypeinPlataform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Earnings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class AngerExp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class ViolenceCriteria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class LegalBack(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class OtherIncome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class LateResponse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

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
