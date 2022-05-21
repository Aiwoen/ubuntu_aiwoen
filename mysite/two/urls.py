from django.urls import path
from two import views

urlpatterns = [

    path('index/', views.index),
    path('addstudent/',views.add_student)
    path('getstudent',views.get_student)
]
