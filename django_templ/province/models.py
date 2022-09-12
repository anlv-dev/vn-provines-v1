from django.db import models


MOI_QUAN_HE = (
    ("BV", 'Ba Vợ'),
    ('MV', 'Mẹ Vợ'),
    ("BR", 'Ba Ruột'),
    ('MR', 'Mẹ Ruột'),
    ('BC', 'Ba Chồng'),
    ('MC', 'Mẹ Chồng'),
    ('CO', 'Con'),
    ('VO', 'Vợ'),
    ('CH', 'Chồng'),
)
GIOI_TINH = (
    ("M", 'Nam'),
    ("F", 'Nữ'),
    ("O", 'Khác'),
)

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
    province = models.ForeignKey(City,on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL, blank=True, null=True)
    ward = models.ForeignKey(Ward,on_delete=models.SET_NULL, blank=True, null=True)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=50, blank=True, null=True)
    house_no = models.CharField(max_length=50)
    used = models.BooleanField(default=True)

    def __str__(self):
        return self.province.name_with_type

class PrivatePhone(models.Model):
    number = models.CharField(max_length=20, blank=True, null=True)
    isActived = models.BooleanField(default=True)

    def __str__(self):
        return self.number

class CompanyPhone(models.Model):
    number = models.CharField(max_length=20, blank=True, null=True)
    phone_type = models.CharField(max_length=5, choices=(
        ("CCN","Chống cháy nổi"),
        ("EXT","Điện thoại nội bộ"),
    ))
    isActived = models.BooleanField(default=True)

    def __str__(self):
        return self.number



class Site(models.Model):
    name = models.CharField(max_length=20,blank=True, null=True)
    short_name = models.CharField(max_length=20,blank=True, null=True)
    fullname = models.CharField(max_length=100,blank=True, null=True)
    eng_name = models.CharField(max_length=100,blank=True, null=True)
    isActived = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name

class Company(models.Model):
    name = models.CharField(max_length=20,blank=True, null=True)
    short_name = models.CharField(max_length=20,blank=True, null=True)
    fullname = models.CharField(max_length=100,blank=True, null=True)
    eng_name = models.CharField(max_length=100,blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, blank=True, null=True)
    isActived = models.BooleanField(default=True)
    
    def __str__(self):
        return self.short_name


class Department(models.Model):
    name = models.CharField(max_length=20,blank=True, null=True)
    short_name = models.CharField(max_length=20,blank=True, null=True)
    fullname = models.CharField(max_length=100,blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    eng_name = models.CharField(max_length=100,blank=True, null=True)
    isActived = models.BooleanField(default=True)
    
    def __str__(self):
        return self.short_name


class RelationshipPerson(models.Model):
    firstname = models.CharField(max_length=20,blank=True, null=True)
    middlename = models.CharField(max_length=20,blank=True, null=True)
    lastname = models.CharField(max_length=20,blank=True, null=True)
    cmnd_no = models.CharField(max_length=20,blank=True, null=True) # Luu cmnd cu
    cccd_no = models.CharField(max_length=20,blank=True, null=True) # Can cuoc cong dan/CMND
    dob = models.DateField()
    moi_quan_he = models.CharField(max_length=20, choices=MOI_QUAN_HE, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GIOI_TINH, blank=True, null=True)
    is_Staff = models.BooleanField(default=False)
    addresses = models.ManyToManyField(Address)
    private_phone = models.ForeignKey(PrivatePhone, on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.firstname + "__" + self.moi_quan_he

class Person(models.Model):
    firstname = models.CharField(max_length=20,blank=True, null=True)
    middlename = models.CharField(max_length=20,blank=True, null=True)
    lastname = models.CharField(max_length=5,blank=True, null=True)
    code = models.CharField(max_length=20,blank=True, null=True)
    phongban = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    cmnd_no = models.CharField(max_length=20,blank=True, null=True) # Luu cmnd cu
    cccd_no = models.CharField(max_length=20,blank=True, null=True) # Can cuoc cong dan/CMND
    gender = models.CharField(max_length=10, choices=GIOI_TINH, blank=True, null=True)
    dob = models.DateField()
    is_Staff = models.BooleanField(default=True)
    nguoi_than = models.ManyToManyField(RelationshipPerson)
    addresses = models.ManyToManyField(Address)
    vo_chung_cty = models.BooleanField(default=False)
    private_phone = models.ForeignKey(PrivatePhone, on_delete=models.SET_NULL, blank=True, null=True)
    company_phone =models.ManyToManyField(CompanyPhone)

    def __str__(self):
        return self.lastname

