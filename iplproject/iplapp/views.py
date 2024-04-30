from django.shortcuts import render,redirect
from .models import Teams
from .forms import TeamModelForm,TeamsForm
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