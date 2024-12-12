
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Developer', 'Developer'),
        ('Viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    organization = models.ForeignKey('auth_app.Organization', on_delete=models.CASCADE, null=True, blank=True)

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    invite_code = models.CharField(max_length=10, unique=True)
