from .models import Address, City, District, Ward
from django import forms

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address        
        fields = ['province','district','ward','street','building','house_no']
        
        widgets = {
            
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