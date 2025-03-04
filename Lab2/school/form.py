from django.forms import ModelForm
from .models import School,Classroom
class SchoolForm(ModelForm):
  class Meta:
    model=School
    fields=["name","number_of_classes","area"]

class ClassroomForm(ModelForm):
  class Meta:
    model=Classroom
    fields=["school","name","area"]
