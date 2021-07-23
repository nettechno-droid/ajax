from django.core import serializers
from django.core.serializers import serialize
from person.forms import PersonForm
from typing import get_args
from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from person.models import PersonModel


# Create your views here.

class PersonView(View):

   def get(self,request):
    persons=PersonModel.objects.all()
    scheme = str(request.scheme)
    get_host = str(request.get_host())
    return render(request,'person/person.html',{'persons':persons, 'scheme':scheme,'get_host':get_host})

   def post(self,request):
    image=request.FILES.get("image")
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    if request.is_ajax():  
        form = PersonForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form_data = form.save()
            ser_data = serializers.serialize('json',[form_data,])
            return JsonResponse({"message":"success","instance" : ser_data}, status=200) 
   
    return JsonResponse({'error':True,'errors':form.errors}, status=400)



class PersonDelete(View):

    def get(self,request,id,*args,**kwargs):
        if PersonModel.objects.filter(id=id):
            model = PersonModel.objects.get(id=id)
            model.delete()
            return JsonResponse({"message":"success"})
        else:
            return JsonResponse({"message":"Wrong request"})