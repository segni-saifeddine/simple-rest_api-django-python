from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employess
from .serialzers import serializerEmployess

class emplist(APIView):
     def get(self, request):
         emply1=employess.objects.all()
         serializer=serializerEmployess(emply1, many=True)
         return Response(serializer.data)

     def post (self):
        pass
