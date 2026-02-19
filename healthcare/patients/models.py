from django.db import models
import uuid

class Patient(models.Model):
    id = models.UUIDField(primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    
    name = models.CharField(max_length = 60)
    
    email = models.EmailField(unique = True)
    
    date_of_birth = models.DateField()
    
    active = models.BooleanField(default = True)
    
    registry_id = models.CharField(max_length = 255, null = True, blank = True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "patients"
        indexes = [
            models.Index(fields =["email"]),
            models.Index(fields = ["registry_id"]),
        ]
        
    def __str__(self):
        return f"{self.name} ({self.id})"
