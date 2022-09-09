from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    name_with_type = models.CharField(max_length=255)
    code = models.IntegerField(unique=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name_with_type


class District(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    name_with_type = models.CharField(max_length=255)
    path = models.CharField(max_length=500)
    path_with_type = models.CharField(max_length=1000)
    code = models.IntegerField()
    parent_code = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name_with_type


class Ward(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    name_with_type = models.CharField(max_length=255)
    path = models.CharField(max_length=500)
    path_with_type = models.CharField(max_length=1000)
    code = models.IntegerField()
    parent_code = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name_with_type
    
class Address(models.Model):
    first_name = models.CharField(max_length=20,blank=True, null=True)
    middle_name = models.CharField(max_length=20,blank=True, null=True)
    last_name = models.CharField(max_length=20,blank=True, null=True)
    province = models.ForeignKey(City,on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL, blank=True, null=True)
    ward = models.ForeignKey(Ward,on_delete=models.SET_NULL, blank=True, null=True)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50)
    used = models.BooleanField(default=True)

    def __str__(self):
        return self.province.name_with_type