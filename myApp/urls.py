from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add_student', views.add_student, name='add_student'),
    path('student_update/<int:pk>', views.student_update, name='student_update'),
    path('student_delete/<int:pk>', views.student_delete, name='student_delete'),
]