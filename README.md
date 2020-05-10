# simple-rest_api-django-python
employments management REST API with Pyhton, Django, Json  and Sqlite

##Setps
toc create a REST API with django,you will typically follow these steps:
1.Set up django
2.Create a model in the database that the Django ORM will manage
3.Serialize the model from step 2
4.Create the URI endpoints to view the serialized data
## 1.Set up django :

1.1 first we have to install django
* `$ pip install Django`
1.2 install django rest-framework:
* `$ pip install Djangorestframework`
1.3 Next let's create a new django project
* `$ django-admin startproject "rest_api" `
1.4 let's make sure it work :
* `$ python manage.py migrate`
And then run the Django server :
* `$ python manage.py`
Go to localhost:8000 and you should see the Django welcome screen!
1.5 Create API AP
To create a new app for our APi we use the commend :
* `$ python manage.py startapp "blog" `
Best practice is to separate your Django project into separate apps when you build something new.
1.6 Add the new app to the INSTALLED_APPS:
Moving to the model setting.py and add the two app:"rest_api " and our app "blog" to the INSTALLED_APPS
1.7 Migrate the DATABASE and create super user
Now after creating the app,we have to tell django to migrate those changes to the DATABASE
* `$ python manage.py migrate`
* `$ python manage.py createsuperuser`
To verify that it works,start up the Django surver,And then navigate to localhost:8000/admin
Log in with your superuser credentials, and you should see the admin dashboard
## 2.Create a model in the database that Django ORM will manage:
2.1 Cretae the models
Move to the app "blog " and open the file "modles".py,it's here where we will make our model
let's make a Databes of employees,each employees has a first anme,a last name and an id
```
class employess(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    id_employ=models.IntegerField()

def __str__(self):
        return self.firstname
```
2.2 Migrate :
whenever we define or change a model, we need to tell Django to migrate those changes.
* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
2.3 Register the employees model with admin site:
```
from django.contrib import admin

from .models import employess

admin.site.register(employess)
```
Now,run the server and create a few employees.

## 3.Serialize the model from step 2 :
first let's create a new file --blog/serialzers.py
Import the employees model
Import the REST Framework serializer
Create a new class that links the employess with its serializer
```
from rest_framework import serializers
from .models import employess

class serializerEmployess(serializers.ModelSerializer):
    class Meta:
        model=employess
        fields='__all__'
```
## 4.Create the URI endpoints to view the serialized data :
Now, all that’s left to do is wire up the URLs and views to display the data!
4.1 views
We need to render the different heroes in JSON format.
in blog/views.py :
```
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employess
from .serialzers import serializerEmployess

class emplist(APIView):
     def get(self, request):
         emply1=employess.objects.all()
         serializer=serializerEmployess(emply1, many=True)
         return Response(serializer.data)

     def post (self):
        pass

```
4.2 Sit URLs
Now we have to to point a URL at the viewset we just created.
in rest_api/urls.py :
```
rom django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employess/', views.emplist.as_view()),

]
```
## Test it out
Run the server again and go to localhost:8000/employees
