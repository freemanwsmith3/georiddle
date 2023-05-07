from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Result(models.Model):
    user = models.CharField(max_length=100, default=None, null=True)
    won = models.BooleanField()
    day = models.IntegerField(null=True)
    points = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]

    )
    month = models.CharField(max_length=100)

    
class Country2(models.Model):
    
    name = models.CharField(max_length=100, primary_key=True)

    continent = models.CharField(max_length=100)

    capital = models.CharField(max_length=100)

    population = models.IntegerField()

    density = models.IntegerField()

    area = models.IntegerField()

    landlocked = models.BooleanField(default =False, null= True)

    lat = models.DecimalField(max_digits=4, decimal_places=1,  null= True)

    long = models.DecimalField(max_digits=4, decimal_places=1,  null= True)
    

    class Meta: 
        ordering = ('name', )

        def __str__(self):
            return self.name



    
class Riddle(models.Model):

    day = models.IntegerField(null=True)
    question = models.CharField(max_length=1024)
    answers = models.ManyToManyField(Country2)
    sort = models.CharField(max_length=100)

