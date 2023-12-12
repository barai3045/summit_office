from rest_framework import generics
from hr.models import Employee, EmployeeOffice, EmployeeTitle, Office, Title
from hr.serializers import EmployeeOfficeSerializer, EmployeeSerializer, EmployeeTitleSerializer, OfficeSerializer, TitleSerializer



# Create your views here.
class OfficeList(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class OfficeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class TitleList(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer 


class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer 


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeTitleList(generics.ListCreateAPIView):
    queryset = EmployeeTitle.objects.all()
    serializer_class = EmployeeTitleSerializer


class EmployeeTitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeTitle.objects.all()
    serializer_class = EmployeeTitleSerializer


class EmployeeOfficeList(generics.ListCreateAPIView):
    queryset = EmployeeOffice.objects.all()
    serializer_class = EmployeeOfficeSerializer


class EmployeeOfficeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeOffice.objects.all()
    serializer_class = EmployeeOfficeSerializer