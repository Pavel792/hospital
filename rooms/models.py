from django.db import models

# Create your models here.


class Articles(models.Model):
    num = models.TextField('Номер')

    name1 = models.TextField('Имя1')
    about1 = models.TextField('Болезнь1')
    temp1 = models.TextField('Температура1')
    date1 = models.DateField('Дата поступления1')

    name2 = models.TextField('Имя2')
    about2 = models.TextField('Болезнь2')
    temp2 = models.TextField('Температура2')
    date2 = models.DateField('Дата поступления2')

    name3 = models.TextField('Имя3')
    about3 = models.TextField('Болезнь3')
    temp3 = models.TextField('Температура3')
    date3 = models.DateField('Дата поступления3')

    name4 = models.TextField('Имя4')
    about4 = models.TextField('Болезнь4')
    temp4 = models.TextField('Температура4')
    date4 = models.DateField('Дата поступления4')

    def __str__(self):
        return f'Палата: {self.num}'

    def get_absolute_url(self):
        return f'/hospital/{self.id}'

    class Meta:
        verbose_name = 'Палата'
        verbose_name_plural = 'Палаты'