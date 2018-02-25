from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name
