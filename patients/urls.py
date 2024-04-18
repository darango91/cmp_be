from django.urls import path
from patients import views

urlpatterns = [
    path("", views.PatientList.as_view(), name="patient-list"),
]