from django.db import models

# Create your models here.

class ContactMassage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    massage = models.TextField()
    
    def __str__(self):
        return self.name