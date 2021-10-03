from django.db import models
        
# Create your models here.

class Books(models.Model):
    name      =  models.CharField(max_length=20)
    author    =  models.CharField(max_length=30)
    pub_date  =  models.DateField(blank=True)
    
    def __str__(self):
        return self.name 

class Fruits(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    count = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='fruits', on_delete=models.CASCADE)
    highlighted = models.TextField()
    def __str__(self):
        return self.name