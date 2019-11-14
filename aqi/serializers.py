from rest_framework.serializers import ModelSerializer
from .models import Aqi,Connection


class AqiSerializer(ModelSerializer):

    class Meta:
        model = Aqi
        fields = '__all__'


class ConnectionSerializer(ModelSerializer):

    class Meta:
        model = Connection
        fields = '__all__'