#here we define business logic for our api the functions how they behave,here we have crud functionalities 
#for our employee

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializer import EmployeeSerializer

class EmployeeAPIView(APIView):
    # Handle GET request (list all employees or get by ID)
    def get(self, request, employee_id=None):
        if employee_id:
            try:
                employee = Employee.objects.get(employee_id=employee_id)
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Employee.DoesNotExist:
                return Response(
                    {"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST request (create a new employee)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle PUT request (update an employee)
    def put(self, request, employee_id=None):
        if not employee_id:
            return Response(
                {"error": "Employee ID is required for update"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)  # partial=True allows updating specific fields
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
            )

    # Handle DELETE request (delete an employee)
    def delete(self, request, employee_id=None):
        if not employee_id:
            return Response(
                {"error": "Employee ID is required for deletion"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            employee.delete()
            return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
            )

