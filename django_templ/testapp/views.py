from django.shortcuts import render

# Create your views here.
def testview(request):
    context = {}
    return render(request,'my_tmp/reg.html', context)