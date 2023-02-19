from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'capital', 'continent')

admin.site.register(models.Continent)

admin.site.register(models.Capital)


admin.site.register(models.Riddle)