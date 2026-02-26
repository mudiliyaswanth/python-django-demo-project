from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
    
from healthcare.vitals.serializers import VitalSignSerializer
from healthcare.vitals.services import VitalSignService


class VitalSignListCreateView(APIView):

    def get(self, request, patient_id):
        vitals = VitalSignService.get_vital_signs(patient_id)
        serializer = VitalSignSerializer(vitals, many=True)
        return Response(serializer.data)


    def post(self, request, patient_id):
        serializer = VitalSignSerializer(data=request.data)

        if serializer.is_valid():
            vital = VitalSignService.add_vital_sign(patient_id, serializer.validated_data)
            return Response(VitalSignSerializer(vital).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VitalSignDetailView(APIView):
    def get(self, request, patient_id, type):
        vital = VitalSignService.get_latest_vital_sign(patient_id, type)
        if not vital:
            return Response({'error':f'Vital Signs not found for {type}'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VitalSignSerializer(vital)
        return Response(serializer.data, status=status.HTTP_200_OK)