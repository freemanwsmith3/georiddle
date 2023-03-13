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

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    
class Currency(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    

class Country(models.Model):

    class CountryObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()


    code = models.CharField(max_length=4, null= True)


    continent = models.ForeignKey(
        Continent, on_delete=models.PROTECT, default=None, null= True)

    capital = models.ForeignKey(
        Capital, on_delete=models.PROTECT, default=None, null= True)

    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, default=None, null= True)

    name = models.CharField(max_length=100)

    languages = models.ManyToManyField(Language)

    borders = models.ManyToManyField('self')

    landlocked = models.BooleanField(default =False, null= True)

    area = models.IntegerField( null= True)

    lat = models.DecimalField(max_digits=4, decimal_places=1,  null= True)
    long = models.DecimalField(max_digits=4, decimal_places=1,  null= True)

    regions = models.ForeignKey(
        Region, on_delete=models.PROTECT, default=None, null= True)
    
    objects = models.Manager() #default 

    countryobjects = CountryObjects() #custom 

    class Meta: 
        ordering = ('name', )

        def __str__(self):
            return self.name


    
class Riddle(models.Model):

    day = models.IntegerField(null=True)
    question = models.CharField(max_length=1024)
    answers = models.ManyToManyField(Country)


