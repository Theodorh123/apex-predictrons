from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    address = models.TextField(blank=True)
    sex_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    sex = models.CharField(max_length=7, blank=False, choices=sex_choice)
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    occupation = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username



