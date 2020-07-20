from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Level(models.Model):
    category = models.CharField(max_length=100, unique=True)
    difficulty_index = models.IntegerField(default=5,validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])

    def __str__(self):
        return self.category



class Topic(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
