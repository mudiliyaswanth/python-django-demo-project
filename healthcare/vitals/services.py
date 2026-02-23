from healthcare.patients.models import Patient
from healthcare.vitals.models import VitalSign

class PatientNotFound(Exception):
    pass

class VitalSignService:
    @staticmethod
    def add_vital_sign(patient_id, validated_data):
        try:
            patient = Patient.objects.get(id=patient_id)
            return VitalSign.objects.create(patient=patient, **validated_data)
        except Patient.DoesNotExist:
            raise PatientNotFound(f'Patient with id {patient_id} not found')
        
    @staticmethod
    def get_vital_signs(patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            return patient.vital_signs.all()
        except Patient.DoesNotExist:
            raise PatientNotFound(f'Patient with id {patient_id} not found')
    
    @staticmethod
    def get_all_vital_signs():
        return VitalSign.objects.all()