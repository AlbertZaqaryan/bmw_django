from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField('Car name', max_length=50)
    img = models.ImageField('Car img', upload_to='media')
    price = models.IntegerField('Car price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'