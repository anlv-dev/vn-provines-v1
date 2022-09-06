from django.db import models

# Create your models here.
# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    house_no = models.CharField(max_length=10)

class City(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    namewithtype = models.CharField(max_length=50)

    def __str__(self):
        return self.namewithtype

class District(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    namewithtype = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    pathwithtype = models.CharField(max_length=50)
    parentcode = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.namewithtype
    
class Ward(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    namewithtype = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    pathwithtype = models.CharField(max_length=50)
    parentcode = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.namewithtype