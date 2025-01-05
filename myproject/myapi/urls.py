from django.urls import path
from .views import EmployeeAPIView


urlpatterns = [
    path('employees/', EmployeeAPIView.as_view(), name='employee-list-create'),  # GET all and POST
    path('employees/<int:employee_id>/', EmployeeAPIView.as_view(), name='employee-detail'),  # GET by ID, PUT, DELETE
]

