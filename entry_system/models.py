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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")

    def __str__(self):
        return self.name


class Log(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="logs")
    
    hostel_id = models.IntegerField(verbose_name="Hostel")

    time = models.DateTimeField(verbose_name="Entry Time")
    
    ACTIVITY_CHOICES = [
        ('EN', "Entry"),
        ('EX', "Exit"),
    ]
    activity = models.CharField(max_length=2, choices=ACTIVITY_CHOICES, verbose_name="Activity")

    def __str__(self):
        return f"Log{self.id}"