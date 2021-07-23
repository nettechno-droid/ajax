from django.shortcuts import render
from django.views import View
from .models import BookModel
from django.http.response import Http404, JsonResponse
from .forms import BookForm
from django.core import serializers


# Create your views here.

class Book(View):
    
    def get(self,request):
        books=BookModel.objects.all()
        form = BookForm()
        scheme = str(request.scheme)
        get_host = str(request.get_host())
        return render(request,'books.html',{'books':books,'form':form, 'scheme':scheme,'get_host':get_host})


    def post(self,request):
       if request.is_ajax():
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form)
            form_data = form.save()
            ser_data = serializers.serialize('json',[form_data,])
            return JsonResponse({"instance" : ser_data}, status=200)
        else:
            return JsonResponse({'error':True,'errors':form.errors}, status=400)


class DeleteBook(View):
    def get(self,request,id,*args,**kwargs):
        if BookModel.objects.filter(id=id):
            model = BookModel.objects.get(id=id)
            print(model)
            print(id)
            model.delete()
            return JsonResponse({"message":"success"})
        else:
            return JsonResponse({"message":"Wrong request"})
            