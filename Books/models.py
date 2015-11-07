from django.db import models
BYADMIN_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)
BYADMIN_CHOICES1 = (
    ('N', 'New Book'),
    ('H', 'High Rated Book'),
    ('M', 'Most Popular Book'),
    
)
# Create your models here.
class Book(models.Model):
    
    Photo=models.ImageField()
    Book_Name=models.CharField(max_length=250)
    ISBN_NBR=models.CharField(max_length=250,unique=True)
    PUB_NAME=models.CharField(max_length=250)
    Author_Name=models.CharField(max_length=250)
    Book_Desc=models.TextField()
    Status=models.CharField(choices=BYADMIN_CHOICES1,default='New Book',max_length=1)
    Rating=models.CharField(choices=BYADMIN_CHOICES,default=1,max_length=1)
    Category=models.CharField(max_length=250)
    Sub_Category=models.CharField(max_length=250)
    download_link=models.URLField(max_length=600)
    
   
        
