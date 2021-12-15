from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# class CustomUser(models.Model):
#     first_name = models.CharField(max_length=32, null=True, blank=True)


class Poll(models.Model):
    title = models.CharField(max_length=128)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'


class ChoiceQuestion(models.Model):
    text = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choice_questions')
    choices = models.ManyToManyField('ChoiceAnswer')
    multiple = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'


class TextQuestion(models.Model):
    text = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='text_questions')
    answers = models.ManyToManyField('TextAnswer')

    def __str__(self):
        return f'{self.text}'


class TextAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE)
    text = models.TextField()


class ChoiceAnswer(models.Model):
    users = models.ManyToManyField(User)
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE)
    text = models.CharField(max_length=128)
