from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name

class Capital(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name



class Country(models.Model):

    class CountryObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()

    options = (
        ('correct', 'Correct'),
        ('incorrect', 'Incorrect')
    )

    continent = models.ForeignKey(
        Continent, on_delete=models.PROTECT, default=1)

    capital = models.ForeignKey(
        Capital, on_delete=models.PROTECT, default=1)

    name = models.CharField(max_length=100)

    status = models.CharField(
        max_length=12, choices = options, default ='incorrect'
    )

    objects = models.Manager() #default 
    countryobjects = CountryObjects() #custom 

    class Meta: 
        ordering = ('name', )

        def __str__(self):
            return self.name
    

class Riddle(models.Model):

    question = models.CharField(max_length=1000)
    answers = models.ManyToManyField(Country)
    date = models.DateField()

class Guess(models.Model):
    user = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT)
    riddle = models.ForeignKey(
        Riddle, on_delete=models.PROTECT)
