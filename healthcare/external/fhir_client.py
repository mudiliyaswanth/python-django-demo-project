import requests

class FHIRClient:
    @staticmethod
    def sync_patient(patient):
        FHIR_BASE_URL = 'https://hapi.fhir.org/baseR4'

        payload = {
            'resourceType': 'Patient',
            'name': [
                {
                    'use': 'official',
                    'family': patient.family_name,
                    'given': [patient.given_name]
                }
            ],
            'dateOfBirth': str(patient.date_of_birth()),
        }
        
        try:
            response = requests.post(f'{FHIR_BASE_URL}/Patient', json=payload, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data.get('id')
        
        except requests.exceptions.RequestException as e:
            raise Exception(f'failed to sync patient: {str(e)}')