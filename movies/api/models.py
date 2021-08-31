from django.db import models

class Movie(models.Model):
    "DB object containing the name and year of release of a movie"
    name = models.CharField(max_length=180)
    year_of_release = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name