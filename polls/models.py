import datetime

from django.db import models # метод привязки до БД
from django.utils import timezone

# МОДЕЛІ В БД

class Question(models.Model):
    # обєкти викристовуються як в БД так і в подальшому коді(описуються тип даних і параметри полів)
    question_text = models.CharField('QUESTION "test"',max_length=200)
    pub_date = models.DateTimeField("date published ' test' ")

    def __str__(self):# текстове відображення даного класу
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text