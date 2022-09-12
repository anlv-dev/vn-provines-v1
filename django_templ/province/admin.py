from django.contrib import admin
from .models import City, District, Ward, Address, Site, Company, Department, Person, RelationshipPerson, PrivatePhone, CompanyPhone,Position


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'province', 'district', 'ward', 'street', 'building', 'house_no', 'used']

class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'slug', 'type', 'name_with_type']
    search_fields = ('name', 'code', 'name_with_type')
    #readonly_fields = ('date_joined', 'last_login')  # make fields immutable
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'slug', 'type', 'name_with_type', 'path', 'path_with_type', 'parent_code']
    search_fields = ('name', 'code', 'name_with_type')


class WardAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'slug', 'type', 'name_with_type', 'path', 'path_with_type', 'parent_code']
    search_fields = ('name', 'code', 'name_with_type')


class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name', 'fullname', 'eng_name', 'isActived' ]
   
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name', 'fullname', 'eng_name', 'site', 'isActived' ]

   
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name', 'fullname', 'company','eng_name', 'isActived' ]

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'middlename', 'lastname', 'phongban','cmnd_no', 'cccd_no', 'dob','gender', 'code', 'private_phone', 'vo_chung_cty', 'is_Staff', ]

class RelationshipPersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'middlename', 'lastname', 'cmnd_no', 'cccd_no', 'dob', 'moi_quan_he', 'gender']


class PrivatePhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'isActived']

class CompanyPhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'phone_type', 'isActived']

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name', 'is_actived']

admin.site.register(Address, AddressAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(RelationshipPerson,RelationshipPersonAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(PrivatePhone,PrivatePhoneAdmin)
admin.site.register(CompanyPhone,CompanyPhoneAdmin)
admin.site.register(Position,PositionAdmin)
