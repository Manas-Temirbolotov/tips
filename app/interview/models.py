from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=255)
    short_answer = models.CharField(max_length=255)
    answer = models.TextField()
    importance = models.IntegerField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


