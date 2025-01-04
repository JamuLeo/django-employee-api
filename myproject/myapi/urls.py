from django.urls import path
from .views import EmployeeCreateView


#ENDPOINTS
urlpatterns = [
    #This is myapi create employee post api
    path('create-employee/', EmployeeCreateView.as_view(), name='create-employee'),
   
]
