from healthcare.patients.models import Patient
from healthcare.external.fhir_client import FHIRClient
from django.shortcuts import get_object_or_404

class PatientService:
    @staticmethod
    def create_patient(validated_data):
        return Patient.objects.create(**validated_data)
    
    @staticmethod
    def get_all_patients():
        return Patient.objects.all()
    
    @staticmethod
    def get_patient_by_id(patient_id):
        return Patient.objects.get(id=patient_id)
    
    @staticmethod
    def update_patient(patient_id, validated_data):
        patient = Patient.objects.get(id=patient_id)
        for attr,value in validated_data.items():
            setattr(patient, attr, value)
        patient.save()
        return patient
        
    @staticmethod
    def partial_update_patient(patient_id, validated_data):
        return PatientService.update_patient(patient_id, validated_data)      
            
    @staticmethod
    def delete_patient(patient_id):
        patient = Patient.objects.get(id=patient_id)
        patient.delete()
    
    @staticmethod
    def sync(patient_id):
        patient = Patient.objects.get(id=patient_id)
        registry_id = FHIRClient.sync_patient()
        patient.registry_id = registry_id
        patient.save()
        return patient