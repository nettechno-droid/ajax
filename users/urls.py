from django.urls import path
from users.views import UserSignUpView,UserLoginView,home,UpdateView,DeleteView,logoff,ForgetPasswordView,ChangePassword,user_detail
# from users.views import , user_detail
# path('user-detail/',user_detail,name='user-detail'),

urlpatterns = [
    path('',home,name='home'),
    path('user_detail/<int:id>',user_detail,name='user_detail'),
    path('signup/',UserSignUpView.as_view(),name='signup'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',logoff,name='logout'),
    path('update/',UpdateView.as_view(),name='update'),
    path('forgetpassword/',ForgetPasswordView.as_view(),name='forget_password'),
    path('delete/<int:id>',DeleteView.as_view(),name='delete'),
    # path('change_password/<int:id>',ChangePassword.as_view(), name="change_password" )   
    path('change_password/<str:key>',ChangePassword.as_view(), name="change_password" )   

]