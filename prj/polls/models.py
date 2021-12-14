from django.db import models


class CustomUser(models.Model):
    first_name = models.CharField(max_length=32, null=True, blank=True)


class Poll(models.Model):
    title = models.CharField(max_length=128)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    description = models.TextField()


class Question(models.Model):
    TYPES = [
        ('text', 'text question'),
        ('choice', 'choosing one option'),
        ('multiple', 'choosing multiple options')
    ]
    text = models.CharField(max_length=256)
    type = models.CharField(max_length=10, choices=TYPES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class TextAnswer(models.Model):
    users = models.ManyToManyField(CustomUser)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()


class ChoiceAnswer(models.Model):
    users = models.ManyToManyField(CustomUser)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    selected = models.BooleanField(default=False)
