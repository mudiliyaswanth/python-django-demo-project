from django.urls import path, include
from healthcare.patients.views import (
    PatientDetailView, PatientListCreateView, PatientSyncView
)

urlpatterns = [
    path('', PatientListCreateView.as_view()),
    path('<uuid:patient_id>/', PatientDetailView.as_view()),
    path('<uuid:patient_id>/sync', PatientSyncView.as_view()),
]