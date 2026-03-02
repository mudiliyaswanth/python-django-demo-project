from healthcare.patients.models import Patient
from healthcare.vitals.models import VitalSign
from healthcare.common.exceptions import NotFoundException

class VitalSignService:
    @staticmethod
    def add_vital_sign(patient_id, validated_data):
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise NotFoundException(f'Patient with id {patient_id} not found')
        return VitalSign.objects.create(patient=patient, **validated_data)
    @staticmethod
    def get_vital_signs(patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise NotFoundException(f'Patient with id {patient_id} not found')
        return patient.vital_signs.all().order_by('-timestamp', 'id')
    
    @staticmethod
    def get_all_vital_signs():
        return VitalSign.objects.all().order_by('id')
    
    @staticmethod
    def get_latest_vital_sign(patient_id, type):
        patient = Patient.objects.filter(id = patient_id)
        if not patient:
            raise NotFoundException
        vital = VitalSign.objects.filter(patient_id=patient_id, type=type).order_by('-timestamp').first()
        if not vital:
            raise NotFoundException(f'Vital Sign of type {type} for patient with id {patient_id} not found')
        return vital