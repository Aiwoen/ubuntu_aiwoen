from adjano.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("two index")
    