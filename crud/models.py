import sys
from itertools import cycle
from django.db import models
from django.core.exceptions import ValidationError 


def validateRut(rut):
    rut = rut.upper()
    rut = rut.replace("-", "")
    rut = rut.replace(".", "")
    aux = rut[:-1]
    dv = rut[-1:]
    try:
        reverse = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reverse, factors))
        res = (-s) % 11
    except:
        raise ValidationError("Invalid rut. Enter a valid RUT") 
    if str(res) == dv:
        return rut
    elif dv == "K" and res == 10:
        return rut
    else:
       raise ValidationError("Invalid rut. Enter a valid RUT") 


class Person(models.Model):
    rut = models.CharField(max_length=20,validators =[validateRut] )
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(blank=False)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.rut, self.name, self.lastName, self.age, self.course
