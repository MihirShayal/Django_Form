from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def djforms(request):
    SUFO=signUpForm()
    d={'sufo':SUFO}

    if request.method=='POST':
        SUFDT=signUpForm(request.POST)
        if SUFDT.is_valid():
            name=SUFDT.cleaned_data['name']
        
            return HttpResponse(str(SUFDT.cleaned_data))
        
    return render(request,'djforms.html',d)
