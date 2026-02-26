from django.db import models
import uuid

class VitalSign(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default =uuid.uuid4,
        editable = False,
    )
    
    patient = models.ForeignKey(
        'healthcare.Patient',
        on_delete = models.CASCADE,
        related_name = 'vital_signs',
    )
    
    TYPE_CHOICES = [
        ('HR', 'Heart Rate'),
        ('BP', 'Blood Pressure'),
        ('TEMP', 'Temperature'),
        ('SPO2', 'Oxygen Saturation')
    ]
    
    type = models.CharField(max_length = 20, choices = TYPE_CHOICES)
    
    value = models.CharField(max_length = 20)
    
    measured_at = models.DateTimeField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = 'vital_signs'    
        indexes = [
            models.Index(fields = ['type']),
            models.Index(fields = ['measured_at']),
        ]
        
    def __str__(self):
        return f'{self.type} for {self.patient.given_name} {self.patient.family_name} at {self.measured_at}: {self.value}'