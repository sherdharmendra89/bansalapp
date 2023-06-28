from django.urls import path, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)


urlpatterns = [
    # Use this route for CRUD operations with api e.g. http://localhost:8000/api/students/ with all methods('GET','POST','DELETE','PUT','PATCH')
    path('api/', include(router.urls)),

    # Use this route for CRUD operations with HTML Templates
    path('students/', student_list, name='student-list'),
    path('students/<int:student_id>/', student_detail, name='student-detail'),
    path('schools/', school_list, name='school-list'),
    path('schools/<int:school_id>/', school_detail, name='school-detail'),
    path('schools/<int:school_id>/update/', update_school, name='update-school'),
    path('schools/<int:school_id>/delete/', delete_school, name='delete-school'),
    path('students/<int:student_id>/update/', update_student, name='update-student'),
    path('students/<int:student_id>/delete/', delete_student, name='delete-student'),
    path('schools/create/', create_school, name='create-school'),
    path('student/create/', create_student, name='create-student'),
    
]