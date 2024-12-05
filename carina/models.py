from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
class Content(models.Model):
    code = models.CharField(max_length=100, unique=True)
    image_url = models.URLField()
    title = models.TextField()
    description = models.TextField()
    link = models.TextField()
    prompt = models.TextField()
    greeting = models.TextField()
    rating = models.PositiveSmallIntegerField(
            validators=[MinValueValidator(1), MaxValueValidator(10)],
            help_text="Rate between 1 and 10",
            default=5,
            null=True,  # if you want to allow no rating
        )
    topic= models.CharField(max_length=200)
    studyNote = models.TextField()
    def __str__(self):
        return self.code