from django.urls import path, include
from healthcare.vitals.views import VitalSignDetailView, VitalSignListCreateView

urlpatterns = [
    path('<uuid:patient_id>/', VitalSignListCreateView.as_view()),
    path('<uuid:patient_id>/latest/<str:type>/', VitalSignDetailView.as_view()),
]