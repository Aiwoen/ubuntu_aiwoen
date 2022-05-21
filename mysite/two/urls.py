from django.urls import path
from two import views

urlpatterns = [

    path('index/', views.index),
    path('addstudent',view.add_student)
]
