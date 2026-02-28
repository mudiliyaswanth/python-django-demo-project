from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from healthcare.common.pagination import StandardResultsSetPagination

from healthcare.patients.serializers import PatientSerializer
from healthcare.patients.services import PatientService


class PatientListCreateView(APIView):

    def get(self, request):
        patients = PatientService.get_all_patients()
        paginator = StandardResultsSetPagination()
        paginated_queryset = paginator.paginate_queryset(patients, request)
        serializer = PatientSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = PatientService.create_patient(serializer.validated_data)
        return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)

    
class PatientDetailView(APIView):
    def get(self, request,patient_id):
        patient = PatientService.get_patient_by_id(patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, patient_id):
        serializer = PatientSerializer(data = request.data)
        serializer.is_valid()
        patient = PatientService.update_patient(patient_id, serializer.validated_data)
        return Response(PatientSerializer(patient).data, status=status.HTTP_200_OK)
        
    
    def patch(self, request, patient_id):
        serializer = PatientSerializer(data = request.data, partial=True)
        serializer.is_valid()
        patient = PatientService.partial_update_patient(patient_id, serializer.validated_data)
        return Response(PatientSerializer(patient).data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, patient_id):
        PatientService.delete_patient(patient_id)
        return Response({'message':f'patient with patient id {patient_id} is deleted'}, status=status.HTTP_200_OK)
    
class PatientSyncView(APIView):
    def post(self, request, patient_id):
        patient = PatientService.sync(patient_id)
        return Response({'message':f'patient with id {(patient_id)} synced successfully', 'registry_id':patient.registry_id}, status=status.HTTP_200_OK)
