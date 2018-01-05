from rest_framework import serializers
from django.conf import settings

#from .models import User
User = settings.AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'blood_group')
