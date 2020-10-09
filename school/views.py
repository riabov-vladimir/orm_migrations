from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


class StudentsList(ListView):
    model = Student
    template = 'school/templates/school/student_list.html'
    ordering = ['group']

# def students_list_view(request):
#     template = 'school/templates/school/student_list.html'
#     context = {
#
#     }
#     pass