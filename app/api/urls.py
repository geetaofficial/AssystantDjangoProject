from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, DepartmentViewSet, StudentCountByDepartmentView


router = routers.DefaultRouter()
router.register('student', StudentViewSet)
router.register('department', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('count/', StudentCountByDepartmentView.as_view(), name='count'),
]
