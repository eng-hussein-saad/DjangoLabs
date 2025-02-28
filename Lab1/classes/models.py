from django.db import models

# Create your models here.
class BaseModel(models.Model):
  id=models.UUIDField(primary_key=True, editable=False, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True


class ClassRoom(BaseModel):
  name = models.CharField(verbose_name="Class Name",max_length=50,unique=True)
  subject=models.CharField(verbose_name="Subject",max_length=50)
  year=models.IntegerField(verbose_name="Year")

class ClassArea(BaseModel):
  name=models.CharField(verbose_name="Area Name",max_length=50,unique=True)
  length=models.IntegerField(verbose_name="Length")
  width=models.IntegerField(verbose_name="Width")