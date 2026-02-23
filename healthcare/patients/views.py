from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthcare.patients.serializers import PatientSerializer
from healthcare.patients.services import PatientService


class PatientListCreateView(APIView):

    def get(self, request):
        patients = PatientService.get_all_patients()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            patient = PatientService.create_patient(serializer.validated_data)
            return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)