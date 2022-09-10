from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddressForm
from .models import City,District,Ward, Address
from django.http import JsonResponse
# Create your views here.


def address_create_view(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        province= request.POST["province"]
        district= request.POST["district"]
        ward= request.POST["ward"]
        print (province)
        print (district)
        print (ward)
        if form.is_valid():
            form.save()
            return redirect('province:add_address')
    context = {
        'form': form
    }
    return render(request,'my_tmp/city.html', context)

def address_edit_view(request,pk):
    address = get_object_or_404(Address, pk=pk)
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('province:edit_address', pk=pk)
    return render(request, 'my_tmp/city.html', {'form': form})


# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})


# AJAX
def getWardsByDistrict(request):
    id_district = request.GET.get('id_district')
    ward = Ward.objects.filter(parent_code__id = int(id_district)).order_by('name_with_type')
    return JsonResponse(list(ward.values('id', 'name_with_type')), safe=False)
    


def getDistrictsByCity(request):
    id_province = request.GET.get('id_province')
    districts = District.objects.filter(parent_code__id = int(id_province)).order_by('name_with_type')    
    return JsonResponse(list(districts.values('id', 'name_with_type')), safe=False)

    