from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    start_date = models.DateField(verbose_name='Дата начала')
    expiration_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPES_OF_ANSWERS = [
        ('text', 'Ответ текстом'),
        ('radio', 'Ответ с выбором одного варианта'),
        ('checkbox', 'Ответ с выбором нескольких вариантов')
    ]

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Добавить в опрос')
    text = models.TextField(verbose_name='Текст вопроса')
    answer_type = models.CharField(max_length=50, choices=TYPES_OF_ANSWERS, verbose_name='Тип вопроса')
    votes = models.IntegerField(default=0, verbose_name='Результаты')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Выберите вопрос', null=True, blank=True)
    choice_text = models.CharField(max_length=200, verbose_name='Вариант ответа', null=True, blank=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text
