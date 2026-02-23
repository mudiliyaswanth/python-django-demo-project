from healthcare.patients.models import Patient
from django.shortcuts import get_object_or_404

class PatientNotFound(Exception):
    pass

class PatientService:
    @staticmethod
    def create_patient(validated_data):
        return Patient.object.create(**validated_data)
    
    @staticmethod
    def get_all_patients():
        return Patient.objects.all()
    
    @staticmethod
    def get_patient_by_id(patient_id):
        try:
            return Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise PatientNotFound(f'Patient with id {patient_id} not found')
    
    @staticmethod
    def update_patient(patient_id, validated_data):
        try:
            patient = Patient.objects.get(id=patient_id)
            for attr,value in validated_data.items():
                setattr(patient, attr, value)
            patient.save()
            return patient
        
        except Patient.DoesNotExist:
            raise PatientNotFound(f'Patient with id {patient_id} not found')    
            
    @staticmethod
    def delete_patient(patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
        except Patient.DoesNotExist:
            raise PatientNotFound(f'Patient with id {patient_id} not found')
    
    