from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


# class StudentsList(ListView):
#     model = Student
#     template = 'school/templates/school/student_list.html'
#     ordering = ['group']

def students_list_view(request):
    template = 'school/student_list.html'

    students = Student.objects.prefetch_related('teacher').all()

    context = {
        'object_list': students.order_by('group')
    }
    return render(request, template, context)
