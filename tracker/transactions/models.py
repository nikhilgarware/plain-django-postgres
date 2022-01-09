from django.db import models
from transactions import constant


class Transaction(models.Model):
    transaction_id = models.IntegerField(unique=True)
    brief_description = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    transaction_type = models.IntegerField(choices=constant.TRANSACTION_TYPE, default=1)
    classification = models.CharField(max_length=255, default="Utility")
    date = models.DateField()
