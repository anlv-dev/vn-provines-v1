from .models import Address, City, District, Ward
from django import forms

# GENDER = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )


# default_city_code_ha_noi = 1
# default_district_code_ba_dinh = 1
CITY_CHOICES = ()
# DISTRICT_CHOICES =()
# WARD_CHOICES =()

cities = City.objects.all()
for city in cities:
    y = (city.code, city.name_with_type),
    CITY_CHOICES += y
# districts = District.objects.filter(parent_code__code = default_city_code_ha_noi).order_by('name_with_type')
# for dist in districts:
#     d = (dist.code, dist.name_with_type),
#     DISTRICT_CHOICES += d
# wards = Ward.objects.filter(parent_code__code = default_district_code_ba_dinh).order_by('name_with_type')
# for ward in wards:
#     w = (ward.code,ward.name_with_type),
#     WARD_CHOICES +=w

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address        
        fields = ['province','district','ward',]
        
        widgets = {
            'province': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                },choices=CITY_CHOICES
            ),
            'district': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                },
            ), 
            'ward': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                },
            ),
                  
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district'].queryset = District.objects.none()
            if 'province' in self.data:
                print('what is this')

            # if 'city' in self.data:
            #     try:
            #         city_id = int(self.data.get('city'))
            #         self.fields['district'].queryset = City.objects.filter(country_id=city_id).order_by('name')
            #     except (ValueError, TypeError):
            #         pass  # invalid input from the client; ignore and fallback to empty City queryset
            # elif self.instance.pk:
            #     self.fields['district'].queryset = self.instance.city.district_set.order_by('name')

