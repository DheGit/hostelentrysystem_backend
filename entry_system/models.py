from django.db import models

# Create your models here.

class Person(models.Model):
    roll = models.BigIntegerField(primary_key=True, verbose_name="Roll Number")
    
    name = models.CharField(max_length=128, verbose_name="Name")
    
    GENDER_CHOICES=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(choices=GENDER_CHOICES, verbose_name="Gender")