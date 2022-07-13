from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

SWAGGER_TAGS = ['main']

STRING = openapi.Schema(type=openapi.TYPE_STRING, description='Edited Meta Data for the document')

class TestView(APIView):
    def get(self, request):
        return Response({
            'status' : 1
        })