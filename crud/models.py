import sys
from itertools import cycle
from django.db import models
from django.core.exceptions import ValidationError

# validateRut is a custom validator is added to verify
# if the rut is valid or not
# if it isn't valid, stops the input data processing
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
    except:  # Indicates if the rut has an invalid type of data
        raise ValidationError("Invalid rut. Enter a valid RUT")
    if str(res) == dv:
        return rut
    elif dv == "K" and res == 10:
        return rut
    else:  # Indicates if the rut is in invalid format
        raise ValidationError("Invalid rut. Enter a valid RUT")

# Here it is set the DB table Person and
# its field restrictions and validators
class Person(models.Model):
    rut = models.CharField(max_length=20, validators=[validateRut])
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(blank=False)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.rut, self.name, self.lastName, self.age, self.course
