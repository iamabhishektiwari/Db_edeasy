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

class RelatedExam(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class McqQuestion(models.Model):
    q_id = models.AutoField(primary_key=True)
    statement = models.TextField()
    category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    answer =  models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    relatedExam = models.ForeignKey(RelatedExam, on_delete=models.CASCADE)

    def __str__(self):
        return self.q_id
