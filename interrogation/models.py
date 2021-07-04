from django.contrib.auth import get_user_model
from django.db import models


class Interrogation(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название опроса', blank=False)
    description = models.TextField(verbose_name='Описание', blank=True)
    start = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата старта')
    stop = models.DateTimeField(verbose_name='Дата окончания', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный?', blank=True)

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        ordering = ['-title']
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    TYPE_OF_QUESTION = [
        ('Text', 'Ответ текстом'),
        ('One option', 'Ответ с выбором одного варианта'),
        ('Several options', 'Ответ с выбором нескольких вариантов'),
    ]
    text = models.TextField(verbose_name='Текст вопроса', blank=False)
    type = models.CharField(max_length=200, verbose_name='Тип опроса', choices=TYPE_OF_QUESTION, default='Text', blank=False)
    interrogation = models.ForeignKey(Interrogation, on_delete='CASCADE', verbose_name='Опрос', default=0, related_name='questions')

    def __str__(self):
        return "{0}".format(self.text)

    class Meta:
        ordering = ['-type']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    interrogation = models.ForeignKey(Interrogation, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.CharField(max_length=4096)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "" + self.question.__str__() + self.choice 