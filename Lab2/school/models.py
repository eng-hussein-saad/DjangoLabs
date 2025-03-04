from django.db import models
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.

class School(models.Model):
  name = models.CharField(
    verbose_name="School Name",
    max_length=50,
    unique=True,
    blank=False,
    null=False
  )
  number_of_classes = models.IntegerField(
    verbose_name="Number of Classes",
    blank=False,
    null=False
  )
  area = models.FloatField(
    verbose_name="Area",
    blank=False,
    null=False
  )

  @property
  def rounded_area(self):
    """Returns the area rounded to 2 decimal places"""
    return float(Decimal(str(self.area)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

  def __str__(self):
    return self.name
  
class Classroom(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")
  name = models.CharField(
    verbose_name="Classroom Name",
    max_length=50,
    blank=False,
    null=False
  )
  area = models.FloatField(
    verbose_name="Area",
    blank=False,
    null=False
  )

  @property
  def rounded_area(self):
    """Returns the area rounded to 2 decimal places"""
    return float(Decimal(str(self.area)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

  def __str__(self):
    return self.name
