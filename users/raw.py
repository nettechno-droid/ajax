# from django.db import models
# import random
# from datetime import datetime
# from django.contrib.auth.models import (
# BaseUserManager, AbstractBaseUser
# )
# # from admin_webapp.function import validate_name
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# class MyUserManager(BaseUserManager):
# def create_user(self, email, password=None):
# """
# Creates and saves a User with the given email, date of
# birth and password.
# """
# if not email:
# raise ValueError('Users must have an email address')

# user = self.model(
# email=self.normalize_email(email),
# )
# user.account_type = 'U'
# user.set_password(password)
# user.save(using=self._db)
# return user

# def create_superuser(self, email, password=None):
# """
# Creates and saves a superuser with the given email, date of
# birth and password.
# """
# user = self.create_user(
# email,
# password=password,
# )
# user.account_type = 'S'
# user.is_admin = True
# user.is_active = True
# user.save(using=self._db)
# return user


# class Account(AbstractBaseUser):
# accounttype = (
# ('S', 'Super Admin'),
# ('A', 'Admin'),
# ('U', 'User'),
# ('C', 'Company User'),)
# email = models.EmailField(
# verbose_name='email address',
# max_length=255,
# unique=True,
# )
# profile_photo = models.ImageField(upload_to='images/', null=True, blank=True)
# account_type = models.CharField(max_length=1,choices=accounttype,default='U')
# mobile_number = models.CharField(max_length=25, unique=True, null=True, blank=True)
# name = models.CharField(max_length=255, null=True, blank=True)
# lastname = models.CharField(max_length=255, null=True, blank=True)
# is_active = models.BooleanField(default=False)
# is_admin = models.BooleanField(default=False)
# facebook_id = models.CharField(max_length=250, null=True, blank=True)
# google_id = models.CharField(max_length=250, null=True, blank=True)
# otp = models.CharField(max_length=6, null=True, blank=True)
# is_verified_phone = models.BooleanField(default=False)
# otp_created = models.DateTimeField(null=True, blank=True)
# countrycode = models.CharField(max_length=9,null=True,blank=True)
# wallet_amount = models.CharField(max_length=255, default="0")
# wallet_updated_at = models.DateTimeField(null=True,blank=True)
# admin_fixed_price = models.CharField(max_length=255,default="0")
# admin_company_percentage = models.CharField(max_length=255,null=True,blank=True)
# admin_user_percentage = models.CharField(max_length=255,null=True,blank=True)
# date_created = models.DateField(null=True,blank=True)
# zipcode = models.CharField(max_length=255,null=True,blank=True)
# is_verified_company = models.BooleanField(default=False)
# is_verified_user = models.BooleanField(default=True)
# is_online = models.BooleanField(default=False)
# enable_disable_ntfn = models.BooleanField(default=False)

# objects = MyUserManager()

# USERNAME_FIELD = 'email'

# def __str__(self):
# return self.email

# def has_perm(self, perm, obj=None):
# "Does the user have a specific permission?"
# # Simplest possible answer: Yes, always
# return True

# def has_module_perms(self, app_label):
# "Does the user have permissions to view the app `app_label`?"
# # Simplest possible answer: Yes, always
# return True

# @property
# def is_staff(self):
# "Is the user a member of staff?"
# # Simplest possible answer: All admins are staff
# return self.is_admin

# def send_otp(self):
# self.otp = random.randint(100000, 999999)
# self.otp_created = datetime.now()
# self.save()

# def clean_fields(self, exclude=None):
# super().clean_fields(exclude=exclude)

# def clean(self):
# if self.name == '':
# raise ValidationError(_('INVALID FORM DATA!.'))



# # ///////////////////////////////////////////////////////////////////////////////login

# LOGIN CODE

# class LoginUser(View):

# def get(self, request, lang):
# # english language.
# if lang == 'en':
# if 'email' in request.session:
# del request.session['email']
# return redirect('/en/loginuser/')
# if 'phone' in request.session:
# del request.session['phone']
# return redirect('/en/loginuser/')
# if 'id' in request.session:
# return redirect('/en/')
# return render(request, 'web_app/en/user_webapp/login.html')
# # arabic language.
# if lang == 'ar':
# pass

# def post(self, request, lang):
# # english language.
# if lang == 'en':
# exists = Account.objects.filter(email=request.POST.get('email'))
# if exists:
# user_obj = Account.objects.get(email=request.POST.get('email'))
# if user_obj.is_active == False:
# messages.add_message(request, messages.INFO, 'Your account is currently deactivated. Please contact support.')
# return redirect('/en/loginuser/')
# elif user_obj.account_type == 'C' and request.POST.get('acctype')=='U':
# messages.add_message(request, messages.INFO, 'Invalid user entry.')
# return redirect('/en/loginuser/')
# elif user_obj.account_type == 'U' and request.POST.get('acctype')=='C':
# messages.add_message(request, messages.INFO, 'Invalid company user entry.')
# return redirect('/en/loginuser/')
# else:
# user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
# if user is not None:
# if user.account_type == 'U' and user.is_active == True:
# login(request, user)
# request.session['id'] = user.id
# get_user = Account.objects.get(id=user.id)
# get_user.is_online = True
# get_user.save()
# return redirect('/en/')
# elif user.account_type == 'C' and user.is_active == True:
# login(request, user)
# request.session['id'] = user.id
# get_user = Account.objects.get(id=user.id)
# get_user.is_online = True
# get_user.save()
# return redirect('/en/')
# else:
# messages.add_message(request, messages.INFO, 'Un-authenticated access, Please contact support!')
# return redirect('/en/loginuser/')
# else:
# messages.add_message(request, messages.INFO, 'Invalid login details!')
# return redirect('/en/loginuser/')
# else:
# messages.add_message(request, messages.INFO, 'Email address not found. Please check and try again!')
# return redirect('/en/loginuser/')



# # //////////////////////////////SignUp

# FOR SIGNUP

# class SignupUser(View):
# def get(self, request, lang):
# # english language.
# if lang == 'en':
# if request.session:
# if 'email' in request.session:
# del request.session['email']
# return redirect('/en/signupuser/')
# if 'phone' in request.session:
# del request.session['phone']
# return redirect('/en/signupuser/')
# if 'id' in request.session:
# return redirect('/en/')
# return render(request, 'web_app/en/user_webapp/register.html')
# # arabic language.
# if lang == 'ar':
# if request.session:
# if 'email' in request.session:
# del request.session['email']
# return redirect('/en/signupuser/')
# if 'phone' in request.session:
# del request.session['phone']
# return redirect('/en/signupuser/')
# if 'id' in request.session:
# return redirect('/en/')
# return render(request, 'web_app/en/user_webapp/register.html')

# def post(self, request, lang):
# # english language.
# if lang == 'en':
# email_exists = Account.objects.filter(email=request.POST.get('email'))
# phone_exists = Account.objects.filter(mobile_number=request.POST.get('phone'))
# if email_exists or phone_exists:
# if email_exists and phone_exists:
# messages.add_message(request, messages.INFO, 'email and phone already exists!')
# elif email_exists:
# messages.add_message(request, messages.INFO, 'email already exists!')
# elif phone_exists:
# messages.add_message(request, messages.INFO, 'phone already exists!')
# return redirect('/en/signupuser/')
# else:
# if request.POST.get('name') == '' or request.POST.get('email') == '' or request.POST.get('code') == '' or request.POST.get('phone') == '' or request.POST.get('password') == '' or request.FILES.get('photo') == None:
# messages.add_message(request, messages.INFO, 'fill complete form!')
# return redirect('/en/signupuser/')
# else:
# request.session['phone'] = request.POST.get('phone')
# details = Account()
# details.account_type = request.POST.get('acctype')
# details.name = request.POST.get('name').capitalize()
# details.lastname = request.POST.get('lastname').capitalize()
# details.email = request.POST.get('email')
# details.countrycode = request.POST.get('code')
# details.mobile_number = request.POST.get('phone')
# details.set_password(request.POST.get('password'))
# if request.FILES.get('photo'):
# details.profile_photo = request.FILES['photo'] if 'photo' in request.FILES else None
# details.date_created = datetime.now()
# details.send_otp()
# details.wallet_amount = '0'
# details.save()
# # admin user
# get_admin = Account.objects.get(account_type='A')
# if details.account_type == 'U':
# admin_notify = NotificationModel()
# admin_notify.title = "New worker joined"
# admin_notify.message = "Worker "+details.name+" "+details.lastname+" has joined Jobshub"
# admin_notify.user = get_admin
# admin_notify.date = datetime.now()
# admin_notify.save()
# if details.account_type == 'C':
# admin_notify = NotificationModel()
# admin_notify.title = "New company user joined"
# admin_notify.message = "Company " + details.name + " " + details.lastname + " has joined Jobshub"
# admin_notify.user = get_admin
# admin_notify.date = datetime.now()
# admin_notify.save()
# Application.objects.get_or_create(user=details,client_type=Application.CLIENT_CONFIDENTIAL,authorization_grant_type=Application.GRANT_PASSWORD)

# # E-MAIL !
# data = Account.objects.get(mobile_number=request.session['phone'])
# subject = 'Django mails!'
# message = f'{request.scheme}://{request.get_host()}/en/verify-otp/?otp={data.otp}'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = [request.POST.get('email'), ]
# send_mail(subject, message, email_from, recipient_list)
# return redirect('/en/success/')