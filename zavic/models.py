import uuid
from django.db import models

class Answer(models.Model):
    customer_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    answers = models.JSONField()
