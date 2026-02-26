from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthcare.patients.serializers import PatientSerializer
from healthcare.patients.services import PatientService


class PatientListCreateView(APIView):

    def get(self, request):
        patients = PatientService.get_all_patients()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            patient = PatientService.create_patient(serializer.validated_data)
            return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDetailView(APIView):
    def get(self, request,patient_id):
        patient = PatientService.get_patient_by_id(patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, patient_id):
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            patient = PatientService.update_patient(patient_id, serializer.validated_data)
            return Response(PatientSerializer(patient).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, patient_id):
        serializer = PatientSerializer(data = request.data, partial=True)
        if serializer.is_valid():
            patient = PatientService.partial_update_patient(patient_id, serializer.validated_data)
            return Response(PatientSerializer(patient).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, patient_id):
        PatientService.delete_patient(patient_id)
        return Response({'message':f'patient with patient id {patient_id} is deleted'}, status=status.HTTP_200_OK)
    
class PatientSyncView(APIView):
    def post(self, request, patient_id):
        try:
            patient = PatientService.sync(patient_id)
            return Response({'message':f'patient with id {(patient_id)} synced successfully', 'registry_id':patient.registry_id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)