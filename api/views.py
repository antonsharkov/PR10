from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Zamena
from .serializers import ZamenaSerializer
import massivs

class ZamenaView(APIView):

    def get(self, request, array, s1, s2):
        zamena = Zamena(array, s1, s2, massivs.Zamena(array, s1, s2))

        serializer_for_request = ZamenaSerializer(instance=zamena)

        return Response(serializer_for_request.data)
