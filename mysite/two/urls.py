from django.urls import path
from two import views

urlpatterns = [

    path('index/', views.index),
    path('addstudent/',views.add_student),
    path('getstudent/',views.get_student),
    path('updatestudent',views.update_student),
    path('deletestudent',views.delete_student),
    path('addstudents/'),views.add_students),
    
    
]
