from django.contrib import admin
from .models import Person #add this to import the Post model
admin.site.register(Person) #add this to register the Post model