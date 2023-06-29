from django.db import models

# Create your models here.
class contact(models.Model) :
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name
