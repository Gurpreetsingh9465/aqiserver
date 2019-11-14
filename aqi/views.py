from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AqiSerializer
from .models import Aqi
from django.conf import settings
import traceback

class AqiApi(APIView):

    def get(self, request, format=None):
        try:
            a = Aqi.objects.all()
            serializers = []
            for i in a:
                serializers.append({
                    'longitude':i.longitude,
                    'latitude':i.latitude,
                    'additionalInfo':i.additionalInfo
                })
            return Response(serializers)
        except Aqi.DoesNotExist:
            return Response(status=404)
    
    def post(self, request, format=None):
        serializer = AqiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)