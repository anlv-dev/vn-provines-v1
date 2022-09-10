from .models import Address, City, District, Ward
from django import forms

# GENDER = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )


# default_city_code_ha_noi = 1
# default_district_code_ba_dinh = 1
# CITY_CHOICES = ()
# # DISTRICT_CHOICES =()
# # WARD_CHOICES =()

# cities = City.objects.all()
# for city in cities:
#     y = (city.code, city.name_with_type),
#     CITY_CHOICES += y
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
        fields = ['first_name','middle_name','last_name','province','district','ward','street','building','house_no']
        
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            'middle_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            'province': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
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
            self.fields['ward'].queryset = Ward.objects.none()
         
            if 'province' in self.data:
                try:
                    province_id = int(self.data.get('province'))
                    district_id = int(self.data.get('district'))
                    self.fields['district'].queryset = District.objects.filter(parent_code__id=province_id).order_by('name')
                    self.fields['ward'].queryset = Ward.objects.filter(parent_code__id=district_id).order_by('name')
                    #if 'district' in self.data:
                        #district_id = int(self.data.get('district'))
                    # district_id = 19
                    #     #print(district_id)
                    # self.fields['ward'].queryset = Ward.objects.filter(parent_code__id=district_id).order_by('name_with_type')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            
            # elif self.instance.pk:
            #      self.fields['district'].queryset = self.instance.province.district_set.order_by('name_with_type')
            #      self.fields['ward'].queryset = self.instance.district.ward_set.order_by('name_with_type')