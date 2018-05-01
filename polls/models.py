import datetime

from django.db import models # метод привязки до БД
from django.utils import timezone


class Question(models.Model):
    # обєкти викристовуються як в БД так і в подальшому коді(описуються тип даних і параметри полів)
    question_text = models.CharField('QUESTION "test"',max_length=200)
    pub_date = models.DateTimeField("date published ' test' ")

    def __str__(self):# текстове відображення даного класу
        return self.question_text

    def was_publised_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text