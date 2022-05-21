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
    