from django.db import models

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()  
    message = models.TextField()  















# from mongoengine import Document, StringField, EmailField

# class Contact(Document):
#     firstname = StringField(max_length=100, required=True)
#     lastname = StringField(max_length=100, required=True)
#     email = EmailField(required=True)
#     message = StringField(required=True)

#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"