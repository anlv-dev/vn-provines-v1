from django.contrib import admin
from .models import City, District, Ward, Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'province', 'district', 'ward', 'street', 'building', 'house_no', 'used']

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


admin.site.register(Address, AddressAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Ward, WardAdmin)
