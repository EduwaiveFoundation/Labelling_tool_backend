from rest_framework import serializers
from .models import glt


class gltSerializer(serializers.ModelSerializer):

    class Meta:
        model=glt
        fields='__all__'
