from django.db import models

class Orders(models.Model):
    company = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    ram = models.FloatField()
    rom = models.FloatField()
    processor = models.CharField(max_length=30)
    price = models.FloatField()
    weight = models.FloatField()
    picture = models.ImageField(upload_to='images',default='')
    document = models.FileField(upload_to='files', default='')