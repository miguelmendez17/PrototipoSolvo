from django.db import models

class Province(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)

class Canton(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE) 

class District(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100) 
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE) 
