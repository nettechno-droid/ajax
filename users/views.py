from django.contrib.auth import authenticate,login,logout
from django.views import View
from users.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password,check_password
from django.core import serializers
from django.http import JsonResponse



def home(request):
    users=User.objects.all()
    return render (request,'home.html',{'users':users})

def logoff(request):
    print("Under Logout")
    sess=request.session['user']
    print("Session for ",sess)
    # request.session['user']='Value updated'
    # print(request.session['user'])
    del sess
    # request.session.pop('user', None)
    logout(request)
    return render(request,'login.html')

def user_detail(request,id):
    print("under details")
    user=User.objects.get(id=id)
    if request.method=='POST':
     return render(request,'user_detail.html',{'user':user})
    return render(request,'user_detail.html',{'user':user})



class UserSignUpView(View):
    def post(self, request):
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password') 
        profile=request.FILES.get('profile') 
        form={
            'email' : email,
        'username':username,
        'password':password,
        'profile':profile
        }
        reg=User.objects.create_user(username=username,email=email,password=password,profile=profile)
        print(reg)
        reg.set_password(password)
        print(profile)
        print(email)
        reg.save()
        login(request, reg)
        request.session['user']=email
        return render(request,'user_detail.html',{'user':reg})

    def get(self, request):
     user=User.objects.all()
     return render(request,'register.html',{'user':user})

class UserLoginView (View):
    
    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email)
        print(password)
        form={
        'email' :email,
        'password':password,
        }
        user=authenticate(request,email=email,password=password)
        print(user)
        if user:
            print("user Exist")
            serialized_user = serializers.serialize('json', [user,])
            # print(serialized_user)
            request.session['user']=serialized_user
            login(request, user)
            # print(user)
            # print("Now Serialized one")
            # serialized_user = serializers.serialize('json', [user,])
            # print(serialized_user)
            request.session['user']=email
            print("User id through session",request.session['user'])

            request.session['user_id'] = user.id
            print("User id through session",request.session['user_id'])

            return render(request,'user_detail.html',{'user':user})
        else:
            print("User Not Exist")
        return render(self.request,'login.html',{'form':form})

    def get(self,request):
        print("UnderGet")
        return render(self.request,'login.html')
     
class UpdateView(View):

    def get(self,request):
     print("User id through session",request.session['user_id'])   
     user = get_object_or_404(User,id=request.session['user_id'])
     context={'user':user}
     return render(request,'update.html',context)

    def post(self,request):
        # print("User id through session in update",request.session['user_id']) 
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password') 
        profile=request.FILES.get('profile') 
        user = get_object_or_404(User,id=request.session['user_id'])
        form={
            'email' : email,
        'username':username,
        'password':password,
        }
        if username is not None:
         user.username=username
        if email is not None:
         user.email=email
        if profile is not None:
         user.profile=profile
        if password is not None:
         user.set_password(password)
        user.save()
        return JsonResponse({'error':False, 'message':'Uploaded Successfully'})

class ForgetPasswordView(View):
   
    def get(self,request):
     return render(request,'forget_password.html')

    def post(self,request):
        email=request.POST.get('email')
        user = User.objects.get(email=email)
        key=user.id
        return redirect ('change_password',key)

class ChangePassword(View):
    
    def get(self,request,key):
     print("Under change password get")
     return render(request,'changing_password.html')

    def post(self,request,key):
        print("Under change password post")
        try:
         user = User.objects.get(id=key)
        except User.DoesNotExist:
          user = None 
        getOtp="1234"
        otp=request.POST.get('otp')
        print(otp)
        password1=request.POST.get('password1')
        print(password1)
        
        password2=request.POST.get('password2')
        print(password2)
        if otp==getOtp and password1==password2  and (password1 and password2 is not None):
         user.set_password(password1)
         user.save()
         print("password changed")
         return redirect('login')
        print("InValid")
        return render(request,'changing_password.html')
    


class DeleteView(View):
    
    def get(self,request,id):
     user = get_object_or_404(User,id=id)
     user.delete()
     return redirect('home')




