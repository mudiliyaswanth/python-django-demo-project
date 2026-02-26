from rest_framework import serializers
from healthcare.patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['id', 'registry_id', 'created_at', 'updated_at']
    
    def validate_family_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Family name cannot be empty or whitespace")
        return value
    
    def validate_given_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Given name cannot be empty or whitespace")
        return value
        
    def validate_date_of_birth(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError('Date of birth cannot be in future')
        return value
    