from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Teams,User_Details
from .forms import TeamModelForm,TeamsForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.

def first_register(request):
    if request.method == "POST":
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw-repeat']
        print(email,psw,psw_repeat)
    return render(request,'first.html')


def register(request):
    if request.method == "POST":
        # f_name = request.POST['f_name']
        # f_nickname = request.POST['f_nickname']
        # f_started_year = request.POST['f_started_year']
        # f_trophies = request.POST['f_trophies']
        # f_logo = request.FILES.get('f_logo')
        # print(request.FILES)
        # print(f_name,f_nickname,f_started_year,f_trophies,f_logo)
        # 1st Way
        # Teams.objects.create(f_name=f_name,f_nickname=f_nickname,f_started_year=f_started_year,f_trophies=f_trophies,f_logo=f_logo)

        # 2nd way
        # team_obj = Teams(f_name=f_name,f_nickname=f_nickname,f_trophies=f_trophies,f_logo=f_logo)
        # team_obj.f_started_year = 2008
        # team_obj.save()

        # 3rd Way
        new_data = {ele:request.POST[ele] for ele in request.POST if ele!='csrfmiddlewaretoken'}
        new_data['f_logo'] = request.FILES['f_logo']

        Teams.objects.create(**new_data)

        # team_obj = Teams(**new_data)
        # team_obj.save()
          
    return render(request,'register.html')

def teams_list(request):
    team_data = Teams.objects.all()
    return render(request,'list.html',{'teams':team_data})


def get_team(request,id):
    team = Teams.objects.get(id=id)
    if request.method == "POST" and request.FILES:
        # 1st Way
        f_name = request.POST['f_name']
        f_nickname = request.POST['f_nickname']
        f_started_year = request.POST['f_started_year']
        f_trophies = request.POST['f_trophies']
        f_logo = request.FILES['f_logo']
        team.f_name = f_name
        team.f_started_year = f_started_year
        team.f_nickname = f_nickname
        team.f_trophies = f_trophies
        team.f_logo = f_logo
        team.save()

        # 2nd Way
        # new_data = {ele:request.POST[ele] for ele in request.POST if ele!='csrfmiddlewaretoken'}
        # new_data['f_logo'] = request.FILES['f_logo']
        # import pdb;pdb.set_trace()
        # Teams.objects.filter(id=id).update(**new_data)
        return redirect('teams_list')
    return render(request,'register.html',{'team':team})

def delete_team(request,id):
    team = Teams.objects.get(id=id)
    team.delete()
    return redirect('teams_list')

def registerteam_modelform(request):
    form = TeamModelForm()
    if request.method == "POST":
        form = TeamModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return redirect('teams_list')
    return render(request,'modelform.html',{'form':form})

def registerteam_form(request):
    form = TeamsForm()
    if request.method == "POST":
        form = TeamsForm(request.POST,request.FILES)
        # print(form.cleaned_data)
        if form.is_valid():
            data = form.cleaned_data # Make sure you used cleaned_data function only after is_valid() function..
            Teams.objects.create(**data)
        else:
            return redirect('teams_list')
    return render(request,'form.html',{'form':form})

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        otp = random.randint(100000,999999)
        user_data = User.objects.create_user(username=username,email=email,password=password,is_staff=True)
        message = f"""Hi {username}, You have been successfully registered with the IPLApp Application. Please use the OTP to verify your account.
        Verification OTP : {otp}"""
        send_mail(subject="Registration Confirmation",message=message,from_email='gsanjeevreddy91@gmail.com',recipient_list=['sanjeevasimply@gmail.com'],fail_silently=True)
        userdetails_data = User_Details.objects.create(user=user_data,mobile=mobile,otp=otp)
        messages.success(request, 'Email with verify OTP is sent.')
        return redirect('verify_otp',userdetails_data.id)
    return render(request,'register_user.html')

def verify_otp(request,id):
    user_info = User_Details.objects.get(id=id)
    if request.method=="POST":
        otp = request.POST['otp']
        if user_info.otp == int(otp):
            messages.success(request,'OTP verified successfully')
            return redirect('teams_list')
        else:
            messages.warning(request,'OTP verification failed.')
            return redirect('verify_otp',id)
    return render(request,'verify_otp.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user_data = User.objects.filter(email=email)
        if user_data:
            if authenticate(username=user_data[0].username,password=password):
                messages.success(request,'Login Successful')
            else:
                messages.warning(request,'Invalid Login Credentials')
        else:
            messages.warning(request,"Email is not existed in the data.")
    return render(request,'login.html')

def forgot_password(request):
    if request.method == "POST":
        email = request.POST['email']
        email_check = User.objects.filter(email=email)
        if email_check:
            otp = random.randint(100000,999999)
            message = f"""Please use the below OTP for password reset
            OTP = {otp}"""
            send_mail(subject="OTP Verification",message=message,from_email='gsanjeevreddy91@gmail.com',recipient_list=['sanjeevasimply@gmail.com'],fail_silently=True)
            user_data = User_Details.objects.get(user__email=email)
            user_data.otp = otp
            user_data.save()
            messages.success(request,'OTP has been sent to registered email id.')
            return redirect('forgot_verify_otp',email_check[0].id)
        else:
            messages.warning(request,"Email doesnot exist, enter correct email.")
    return render(request,"forgot_password.html")


def forgot_verify_otp(request,id):
    if request.method == "POST":
        otp = request.POST['otp']
        user_data = User_Details.objects.get(user__id=id)
        print(user_data)
        print(user_data.otp)
        if user_data.otp == int(otp):
            messages.success(request,"OTP verification successful")
            return redirect('update_password',id)
        else:
            messages.warning(request,"Please enter Correct OTP")
    return render(request,'forgot_verify_otp.html')


def update_password(request,id):
    if request.method == "POST":
        password = request.POST['password']
        user_data = User.objects.get(id=id)
        user_data.set_password(password)
        user_data.save()
        messages.success(request,"Password Updated")
        return redirect('login_user')
    return render(request,'update_password.html')

















