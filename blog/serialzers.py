from rest_framework import serializers
from .models import employess

class serializerEmployess(serializers.ModelSerializer):
    class Meta:
        model=employess
        fields='__all__'
