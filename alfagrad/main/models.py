from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class LastProjects(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='static/images/', max_length=100)

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Последний проэкт'
        verbose_name_plural = 'Последние проэкты'


class BaseLevel(models.Model):
    
    title = models.CharField(verbose_name='Название 2 ' ,max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=400, help_text='Возможно ввести только до 400 символов')
    first_picture = models.ImageField(verbose_name='фотография 1', upload_to='static/images/', max_length=100)
    first_text = models.CharField(verbose_name='первый скрипт', max_length=100)
    second_picture = models.ImageField(verbose_name='фотография 2', upload_to='static/images/', max_length=100)
    second_text = models.CharField(verbose_name='второй скрипт', max_length=100)
    third_picture = models.ImageField(verbose_name='фотография 3', upload_to='static/images/', max_length=100)
    third_text = models.CharField(verbose_name='третий скрипт', max_length=100)


    def save(self, *args, **kwargs): 
        obj = BaseLevel.objects.first()
        if obj == None:
            super(BaseLevel, self).save(*args, **kwargs)
        else:
            pass 

    def delete(self, *args, **kwargs):
        self.first_picture.delete()
        self.second_picture.delete()
        self.third_picture.delete()
        super().delete(*args, **kwargs)


class Location(models.Model):
    country = models.CharField(verbose_name='Страна', max_length=35)
    city = models.CharField(verbose_name='город',max_length=35)
    index = models.CharField(verbose_name='индекс',max_length=35)
    street = models.CharField(verbose_name='улица',max_length=35)

    class Meta:
        verbose_name = 'Местоположение'

    def save(self, *args, **kwargs): 
        obj = Location.objects.first()
        if obj == None:
            super(Location, self).save(*args, **kwargs)
        else:
            pass 

    def __str__(self):
        return self.street



class Contacts(models.Model):
    phone = PhoneNumberField(verbose_name='номер телефона', null=False, unique=True, blank=True)
    email = models.EmailField(verbose_name='электронная почта', max_length=254, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.phone}, {self.email}'


