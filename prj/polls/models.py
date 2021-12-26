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

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class ChoiceQuestion(models.Model):
    text = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choice_questions')
    multiple = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Вопрос с выбором варианта'
        verbose_name_plural = 'Вопросы с выбором варианта'


class TextQuestion(models.Model):
    text = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='text_questions')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Текстовый вопрос'
        verbose_name_plural = 'Текстовые вопросы'


class TextAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='text_answers')
    question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE, related_name='text_answers')
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Текстовый ответ'
        verbose_name_plural = 'Текстовые ответы'


class ChoiceAnswer(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name='choice_answers')
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE, related_name='choice_answers')
    text = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Ответ с выбором'
        verbose_name_plural = 'Ответ с выбором'
