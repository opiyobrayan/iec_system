from django.shortcuts import render

# Create your views here.
def home(request):

  from django.shortcuts import render
from .models import IecMaterial
from .forms  import IecMaterialForm
from django.http import HttpResponse 
from datetime import date

today = date.today()
today=today.strftime("%Y-%m-%d")
# Create your views here.
def home(request):
    iec_materials=IecMaterial.objects.all()
   
   
    if request.method== 'POST':
        forms=IecMaterialForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponse("Request submitted successfuly ")         
    else:
        forms=IecMaterialForm()

    return render(request,'home.html',{'iec_materials':iec_materials,'form':forms})

def request(request):
    
    today = date.today()
    today=today.strftime("%Y-%m-%d")
    time=request.GET.get('request')
    name=request.GET.get('names')
    print(name)
    print(time)
   
    your_data=IecMaterial.objects.filter(name=name)
    
   
        
    

   
    return render (request,'request.html',{'data':your_data})