from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddressForm
from .models import City,District,Ward, Address
from django.http import JsonResponse
# Create your views here.


def address_create_view(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('province:add_address')
    context = {
        'form': form
    }
    return render(request,'my_tmp/city.html', context)

def address_edit_view(request):
    pass


# AJAX
def getWardsByDistrict(request):
    id_district = request.GET.get('id_district')
    ward = Ward.objects.filter(parent_code__id = id_district).order_by('name_with_type')
    return JsonResponse(list(ward.values('code', 'name_with_type')), safe=False)
    


def getDistrictsByCity(request):
    id_province = request.GET.get('id_province')
    districts = District.objects.filter(parent_code__id = id_province).order_by('name_with_type')
    
    return JsonResponse(list(districts.values('id', 'name_with_type')), safe=False)

    