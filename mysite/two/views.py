import random
from django.http import HttpResponse
from django.shortcuts import render

from two.models import Student


# Create your views here.
def index(request):
    return HttpResponse("two index")
    
def add_student(request):

    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(100)
    student.save()

    return HttpResponse("Add Success %s" % student.s_name)
    
def get_student(request):

    students = Student.objects.all()
    
    for student in students:
        print(student.s_name)

    context = {
    
        "hobby":"test",
        "students":students
    }

    return render(request, 'student.html', context=context)
    
def update_student(request):
    
        student = Student.objects.get(pk=2)
        student.s_name = 'Jack'
        student.save()
    
    return HttpResponse("Update Success")