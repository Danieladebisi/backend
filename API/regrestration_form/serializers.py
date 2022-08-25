from rest_framework import serializers
from .models import Registered_student




class Registered_studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registered_student
        fields=['id', 'first_name', 'last_name', 'email', 'address', 'phone', 'course', 'center', 'mode']
