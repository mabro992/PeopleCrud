# Crud/views.py
from rest_framework import viewsets          # add this
from PeopleCrud.serializers import PersonSerializer      # add this
from .models import Person                     # add this
        
class PersonView(viewsets.ModelViewSet):       # add this
  serializer_class = PersonSerializer          # add this
  queryset = Person.objects.all()              # add this