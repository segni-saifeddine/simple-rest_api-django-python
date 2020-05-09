from django.db import models

class employess(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    id_employ=models.IntegerField()

def __str__(self):
        return self.firstname
