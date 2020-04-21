# Crud/views.py
from rest_framework import viewsets          
from PeopleCrud.serializers import PersonSerializer      
from .models import Person                     
from rest_framework.response import Response
from rest_framework import status

# PersonView set the view to receive the person json data
class PersonView(viewsets.ModelViewSet):       
    serializer_class = PersonSerializer          
    queryset = Person.objects.all()              
    # The DELETE operation is overwritten to
    # return an '200 ok' response when a person
    # is successfully deleted from the DB
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)
