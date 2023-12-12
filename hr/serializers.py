from rest_framework import serializers
from hr.models import Employee, EmployeeOffice, EmployeeTitle, Office, Title

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTitle
        fields = "__all__"


class EmployeeOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeOffice
        fields = "__all__"
