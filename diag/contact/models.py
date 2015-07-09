from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    email = models.EmailField()

