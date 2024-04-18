# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Models and Serializers
from patients.models import Patient
from patients.serializers import PatientSerializer


class PatientList(APIView):
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
