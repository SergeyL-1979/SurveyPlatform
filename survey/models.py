from django.conf import settings
from django.db import models
from django.utils.text import slugify

from users.models import User


class Question(models.Model):
    title = models.CharField(max_length=4096)
    text = models.TextField(null=False, verbose_name='Текст')
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class CheckQuestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)
    survey_viewed = models.BooleanField(default=False)


class Favorites(models.Model):
    """
Избранное класса (модели.Модель):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Связь внешнего ключа с моделью User
    анкета = models.ForeignKey(Questionnaire, on_delete=models.CASCADE) # Связь внешнего ключа с моделью анкеты
    date_of_creation = models.DateTimeField(auto_now_add=True) # Дата и время создания избранного
    Like_status = models.BooleanField(default=False) # Логическое поле для статуса лайка
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    like_rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг')
    like_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def like(self):
        self.like_rating += 1
        self.save()

    def dislike(self):
        self.like_rating -= 1
        self.save()

    # def get_likes(self):
    #     return self.like
