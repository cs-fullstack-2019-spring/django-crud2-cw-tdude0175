from django.db import models

# Create your models here.

# Name
# email
# Phone Number

class ContactModel(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.BigIntegerField(default=0)

    def __str__(self):
        return self.name