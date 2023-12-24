from .models import *
from rest_framework.serializers import ModelSerializer


class MuallifSerializer(ModelSerializer):
    class Meta:
        model = Muallif
        fields = '__all__'


class MaqolaSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'
