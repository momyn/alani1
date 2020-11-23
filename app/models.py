from django.conf import settings
from django.db import models
import datetime



class Category(models.Model):
    title = models.CharField('Загаловок', max_length=150)
    image = models.ImageField('Картинка', upload_to='product/%Y/%m/%d', blank=False)
    menu = models.BooleanField(default=False, null=True, blank=True)
    slug = models.CharField('Ссылка', max_length=150, db_index=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField('Загаловок', max_length=150)
    title = models.TextField('Описание', max_length=350)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField('Картинка', upload_to='product/%Y/%m/%d', blank=False)
    slug = models.CharField('Ссылка', max_length=150, db_index=True, blank=True, unique=True)
    available = models.BooleanField('Отключить товар', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)




class TextProduct(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='produkt',
                                 on_delete=models.CASCADE)
    name = models.CharField('Загаловок', max_length=150)
    title = models.TextField('Описание', max_length=350)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    slug = models.CharField('Ссылка', max_length=150, db_index=True, blank=True, unique=True)
    available = models.BooleanField('Отключить товар', blank=True, default=True)

    class Meta:
        verbose_name = 'Текстовое меню'
        verbose_name_plural = 'Текстовое меню'
        index_together = (('id', 'slug'),)




class Slider(models.Model):
    name = models.CharField('Загаловок', max_length=150)
    title = models.TextField('Текст', max_length=350)
    image = models.ImageField('Картинка', upload_to='product/%Y/%m/%d', blank=True)
    sale = models.CharField('Текст на кнопке', max_length=100)
    slug = models.CharField('Ссылка', max_length=150, db_index=True, unique=True)
    available = models.BooleanField('Отключить товар', default=True)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'



class Info(models.Model):
    image = models.ImageField('Логотип', upload_to='product/%Y/%m/%d', blank=True)
    image1 = models.ImageField('Нижний логотип', upload_to='product/%Y/%m/%d', blank=True)
    insta = models.CharField('Название соц сети 1',max_length=100, blank=True)
    insta2 = models.CharField('Название соц сети 2', max_length=100, blank=True)
    insta3 = models.CharField('Название соц сети 3', max_length=100, blank=True)
    slug = models.URLField('Ссылка на соц сети 1', blank=True)
    slug2 = models.URLField('Ссылка на соц сети 2', blank=True)
    slug3 = models.URLField('Ссылка на соц сети 3', blank=True)


    class Meta:
        verbose_name = 'Редатировать сайт'
        verbose_name_plural = 'Редатирование сайта'


