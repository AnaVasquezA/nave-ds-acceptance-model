import uuid
from django.db import models

class Answer(models.Model):
    customer_rfc = models.CharField(primary_key = True, max_length=50, editable=False)
    answers = models.JSONField()
    result = models.CharField(max_length=30, null=True)
