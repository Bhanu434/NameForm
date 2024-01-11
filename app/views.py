from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def Name(request):
    ENFO=NameForms()
    d={'ENFO':ENFO}
    if request.method=='POST':
        NFO=NameForms(request.POST)
        if NFO.is_valid():
            return HttpResponse(str(NFO.cleaned_data))
    return render(request,'NameForm.html',d)