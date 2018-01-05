from django.db import models


class Cortege(models.Model):
    date = models.DateField(required=True)
    headcount = models.IntegerField(blank=True)
    distance = models.CharField(required=True)
    address = models.CharField
