from django.urls import path, include
from healthcare.patients.views import PatientListCreateView

urlpatterns = [
    path('', PatientListCreateView.as_view()),
]