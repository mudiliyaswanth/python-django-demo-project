from rest_framework import serializers
from healthcare.patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all_'
        read_only_fields = ['id', 'registry_id', 'created_at', 'updated_at']
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Name cannot be empty or whitespace')
        return value
    
    def validate_date_of_birth(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError('Date of birth cannot be in future')
        return value
    