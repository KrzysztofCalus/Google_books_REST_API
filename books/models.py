from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Book(models.Model):
    book_id = models.CharField(max_length=256, primary_key=True)
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=256)
    published_date = models.CharField(max_length=4)
    categories = ArrayField(models.CharField(max_length=256, blank=True, null=True))
    average_rating = models.CharField(max_length=20, blank=True, null=True)
    ratings_count = models.PositiveIntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)


def __str__(self):
    return self.title
