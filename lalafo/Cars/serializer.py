from rest_framework import serializers
from .models import *

class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'title_name', 'description', 'price', 'type_change','image', 'color', 'video', 'year','created_date','volume',]