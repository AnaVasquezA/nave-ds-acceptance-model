import uuid
from django.db import models

class Answer(models.Model):
    customer_rfc = models.CharField(primary_key = True, max_length=50, editable=False)
    customer_name = models.CharField(max_length=100, null=True)
    answers = models.JSONField()
    result = models.CharField(max_length=30, null=True)
    moral = models.IntegerField(null=True)
    legal = models.IntegerField(null=True)
    indifferent = models.IntegerField(null=True)
    corrupt = models.IntegerField(null=True)
