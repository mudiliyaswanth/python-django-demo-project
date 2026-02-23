from django.urls import path, include
from healthcare.vitals.views import VitalSignListCreateView

urlpatterns = [
    path('<uuid:patient_id>/', VitalSignListCreateView.as_view()),
]