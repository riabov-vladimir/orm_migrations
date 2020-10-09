from django.urls import path

from school.views import students_list_view

urlpatterns = [
    # path('', StudentsList.as_view()),
    path('', students_list_view, name='students')
]
