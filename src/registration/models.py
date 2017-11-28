from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=20)
# Create your models here.
