from rest_framework import serializers
from .models import category
from .models import labelled_img

class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model=category
        fields='__all__'


class labelled_imgSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=labelled_img
        fields='__all__'
