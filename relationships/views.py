from django.shortcuts import render
from django.views import View


# Create your views here.

class Relation(View):
    
    def get(self,request):
        return render(request,'relation_test.html')
        
    def post(self,request):
      return render(request,'relation_test.html')
       
    
    
