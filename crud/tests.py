from django.test import TestCase
from crud.models import Person
from crud.views import PersonView
from rest_framework.test import APIRequestFactory
from django.urls import reverse, resolve

# Create your tests here.


class PersonTestCase(TestCase):
    def testPost(self):
        factory = APIRequestFactory()
        request = factory.post('/api/people/', {'rut': "12345678-5",
                                                'name': "Test",
                                                'lastName': "Testera",
                                                'age': 33,
                                                'course': "1st grade"})

    def testGet(self):
        factory = APIRequestFactory()

        view = PersonView.as_view(actions={'get': 'retrieve'})
        person = Person(rut="12345678-5",
                        name="Test",
                        lastName="Testera",
                        age=33,
                        course="1st grade")
        person.save()
        request = factory.get('/api/people/')
        response = view(request, pk=person.pk)
        self.assertEqual(response.status_code, 200)

    def testPut(self):
        factory = APIRequestFactory()
        request = factory.put('/api/people/1/', {'rut': "12345678-5",
                                                 'name': "Test",
                                                 'lastName': "Testera",
                                                 'age': 33,
                                                 'course': "1st grade"})
