from django.urls import path, include
from classes.views import home,name,retrieve_classroom

urlpatterns = [
  path('', home, name='home'),
  path('<str:name>', name, name='name'),
  # path('classroom/<str:class_name>', retrieve_classroom, name='retrieve_classroom'), 
  path('classroom/', retrieve_classroom, name='retrieve_classroom'), 

]