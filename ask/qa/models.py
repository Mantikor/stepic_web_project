from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateField()
  rating = models.IntegerField()
  author = medels.ForeignKey(User)
  likes = models.TextField()
  
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField()
  question = models.ForeignKey(Question)
  author = medels.ForeignKey(User)
