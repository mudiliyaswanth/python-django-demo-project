from django.urls import path, include

urlpatterns = [
    path('healthcare/', include('healthcare.urls')),
    
]