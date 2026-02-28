from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from healthcare.common.pagination import StandardResultsSetPagination
    
from healthcare.vitals.serializers import VitalSignSerializer
from healthcare.vitals.services import VitalSignService

class VitalSignListCreateView(APIView):

    def get(self, request, patient_id): 
        vitals = VitalSignService.get_vital_signs(patient_id)
        paginator =  StandardResultsSetPagination()
        paginated_queryset = paginator.paginate_queryset(vitals, request)
        serializer = VitalSignSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, patient_id):
        serializer = VitalSignSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vital = VitalSignService.add_vital_sign(patient_id, serializer.validated_data)
        return Response(VitalSignSerializer(vital).data, status=status.HTTP_201_CREATED)
    
class VitalSignDetailView(APIView):
    def get(self, request, patient_id, type):
        vital = VitalSignService.get_latest_vital_sign(patient_id, type)
        serializer = VitalSignSerializer(vital)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AllVitalSignsView(APIView):
    def get(self, request):
        all_vitals = VitalSignService.get_all_vital_signs()
        paginator = StandardResultsSetPagination()
        paginated_queryset = paginator.paginate_queryset(all_vitals, request)
        serializer = VitalSignSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data, status=status.HTTP_200_OK)