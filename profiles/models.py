from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    years_of_service = models.CharField(max_length=200)
    story = models.CharField(max_length=1000)
    goal = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    def __str__(self):
        return self.name
        
class Charity(models.Model):
    charity_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    goal = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    def __str__(self):
        return self.charity_name