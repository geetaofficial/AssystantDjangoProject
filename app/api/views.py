from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Student, Department
from .serializers import StudentSerializer, DepartmentSerializer
from django.db.models import Count, F


class StudentViewSet(ModelViewSet):
    """Student Model Viewset"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DepartmentViewSet(ModelViewSet):
    """Department Model Viewset"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StudentCountByDepartmentView(APIView):
    """Count Student as per Department"""

    def get(self, request, format=None):
        s = Student.objects.values('departments_id').order_by('departments_id').annotate(department=F(
            'departments__dept_name'), student_count=Count('departments_id')).values('department', 'student_count')
        return Response(s)
