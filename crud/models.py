from django.db import models
class Person(models.Model):
 rut = models.CharField(max_length=20)
 name = models.CharField(max_length=20)
 lastName = models.CharField(max_length=20)
 age=models.IntegerField(blank=False)
 course=models.CharField(max_length=50)

 
 def __str__(self):
  return self.rut,self.name,self.lastName,self.age,self.course