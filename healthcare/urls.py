from django.urls import path, include

urlpatterns = [
    # patient-centric APIs
    path('patients/', include('healthcare.patients.urls')),
    path('vitals/', include('healthcare.vitals.urls')),
]