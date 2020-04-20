# Crud/serializers.py
from rest_framework import serializers
from crud.models import Person

# PersonSerializer convert the model instance to
# python datatype
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'rut', 'name', 'lastName', 'age', 'course')
