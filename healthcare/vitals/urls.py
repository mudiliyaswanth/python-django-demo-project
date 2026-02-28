from django.urls import path, include
from healthcare.vitals.views import VitalSignDetailView, VitalSignListCreateView, AllVitalSignsView

urlpatterns = [
    path('', AllVitalSignsView().as_view(), name = 'all-vitals'),
    path('<uuid:patient_id>/', VitalSignListCreateView.as_view(), name = 'patient-vitals'),
    path('<uuid:patient_id>/latest/<str:type>/', VitalSignDetailView.as_view(), name = 'latest-patient-vital'),
]