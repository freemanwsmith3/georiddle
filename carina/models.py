from django.db import models


class Content(models.Model):
    code = models.CharField(max_length=100, unique=True)
    image_url = models.URLField()
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.code