from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=250)
    developer = models.CharField(max_length=250)

    def __str__(self):
        return self.name
