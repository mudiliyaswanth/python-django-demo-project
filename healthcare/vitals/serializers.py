from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from healthcare.vitals.models import VitalSign

class VitalSignSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=VitalSign.TYPE_CHOICES)
    
    class Meta:
        model = VitalSign
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        
    def validate(self, data):
        vital_type = data.get('type')
        vital_value = data.get('value')
        
        # Normalize type to uppercase
        if vital_type:
            vital_type = vital_type.upper()
            data['type'] = vital_type  # update data so ChoiceField works

        try:
            if vital_type == 'HR':
                value = int(vital_value)
                if value < 30 or value >200:
                    raise ValidationError('Heart Rate must be between 30 and 200 bpm.')
            
            elif vital_type == 'BP':
                if '/' not in vital_value:
                    raise ValidationError('Blood Pressure must be in format systolic/diastolic, e.g. 120/80')
                systolic, diastolic = vital_value.split('/')
                systolic, diastolic = int(systolic), int(diastolic)
                if systolic <50 or systolic > 250:
                    raise ValidationError('Systolic Blood Pressure must be between 50 and 250 mmHg')
                if diastolic < 30 or diastolic > 150:
                    raise ValidationError('Diastolic Blood Pressure must be between 30 and 150 mmHg')

            elif vital_type == 'TEMP':
                value = float(vital_value)
                if value < 30.0 or value > 45.0:
                    raise ValidationError('Temperature must be between 30.0 and 45.0 °C')
            
            elif vital_type == 'SPO2':
                spo2 = int(vital_value)
                if spo2 < 70 or spo2 > 100:
                    raise ValidationError('Oxygen Saturation must be between 70% and 100%')
            
            else:
                raise ValidationError('Invalid vital sign type')
        
        except ValueError:
            raise ValidationError('Heart Rate must be in integer format')
        
        return data