# PeopleCrud
A CRUD REST-API for persons managament. Developed using django-rest framework in Python 3.7. Deployed usign Google Coud Platform for DJANGO and API-BACK

Deployed site: https://back-api-dot-people-api-275001.uc.r.appspot.com/api/people/

# To run de application locally:
- Clone the repository
- Go to the command line and enter: pip install asgiref, Django, django-filter, djangorestframework, Markdown, pkg-resources, pytz,  sqlparse
- Open the cloned repo and in the console execute the following commands for a proper project installation:
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py createsuperuser (to set an super user)
- To start the app execute the following commands:
  - python manage.py test
  - python manage.py runserver
  
 # CRUD Endpoints:
 - **GET ~/api/people/** -> Gets all the persons data
 - **GET ~/api/people/id** -> Gets a person data given his id
 - **POST ~/api/people/ {JSON Data}** -> Inserts a new person in the DB
 - **PUT ~/api/people/id/ {JSON Data}** -> Updates a person data given the id and the json
 - **DELETE ~/api/people/id/** -> Deletes a person given his id
