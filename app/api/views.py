from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Student, Department
from .serializers import StudentSerializer, DepartmentSerializer
from django.db.models import Count, F


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StudentCountByDepartmentView(APIView):
    def get(self, request, format=None):
        s = Student.objects.values('departments_id').order_by('departments_id').annotate(department=F('departments__dept_name'),student_count=Count('departments_id')).values('department','student_count')
        return Response(s)
