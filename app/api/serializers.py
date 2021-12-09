from rest_framework import serializers
from app.models import Department, Student


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # departments = serializers.HyperlinkedRelatedField()
    departments = DepartmentSerializer()
    class Meta:
        model = Student
        fields = ['std_id', 'first_name', 'last_name', 'full_name','departments']
        read_only_fields = ['full_name']
        depth = 1
        


