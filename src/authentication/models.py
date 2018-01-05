import os
from django.db import models
from custom_user.models import AbstractEmailUser


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class User(AbstractEmailUser):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    primary_contact_number = models.CharField(max_length=10)
    secondary_contact_number = models.CharField(max_length=10)
    facebook_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(max_length=200, blank=True)
    blood_group = models.CharField(max_length=3, blank=True)
    profile_pic = models.ImageField(
        upload_to=get_image_path, blank=True, null=True)

    def __str__(self, *args, **kwargs):
        return '{} {} {}'.format(self.first_name, self.last_name, self.id)
