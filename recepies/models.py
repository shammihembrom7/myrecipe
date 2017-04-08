from django.db import models

# Create your models here.

from djangotoolbox.fields import ListField, EmbeddedModelField,DictField


class Recipe(models.Model):
    _DATABASE = "records"

    title = models.CharField(max_length=20)
    recipe = models.TextField()
    author = DictField()
    reviews = ListField(EmbeddedModelField('Review'))

class Review(models.Model):
    _DATABASE = "records"

    review = models.TextField()
    user = DictField()
