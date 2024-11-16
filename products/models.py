from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField( default=True )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True)
    puplish_date = models.DateField( default=datetime.now )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['puplish_date']
    
    


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2, null=True,blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    active = models.BooleanField( default=True )
    puplish_date = models.DateField( default=datetime.now )
    brand_name = models.CharField(max_length=150, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,blank=True)

    


    def __str__(self):
        return f'{self.name} - {self.category}'
    
    class Meta:
        ordering = ['puplish_date']