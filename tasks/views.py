from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.models import Member,Trainer,MembershipPlan
from tasks.forms import MemberForm,PlanForm,TrainerForm
from django.db.models import Q,Count

# Create your views here.
def home(request):
    mem = Member.objects.count()
    plan = MembershipPlan.objects.count()
    train = Trainer.objects.count()


    return render(request, "base.html", {
        "m": mem,
        "p": plan,
        "t": train
    })


def home2(request):
    query = request.GET.get('q', '') 
    if query:
        members = Member.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        )
    else:
        members  = Member.objects.all()
    return render(request,"memberlist.html",{"members":members})


def home3(request):
    form = MemberForm()
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("member_list")
    return render(request,"member_from.html",{"form":form})

def M_update(request,id):
    member = Member.objects.get(id=id)
    form = MemberForm(instance=member)
    if request.method == "POST":
        form = MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    return render(request,"member_from.html",{"form":form})

def  M_Delet(request,id):
    if request.method == "POST":
        member = Member.objects.get(id=id)
        member.delete()
        return redirect("member_list")
    else:
        return redirect ("member_list")
        

def home4(request):
    plans = MembershipPlan.objects.all()
    return render(request,"plan_list.html",{"plans":plans})

def Planform(request):
    plans = PlanForm()
    if request.method =="POST":
        plans = PlanForm(request.POST)
        if plans.is_valid():
            plans.save()
            return redirect("plan_list")
    return render(request,"plansform.html",{"plans":plans})

def UpdatePlanform(request,id):
    planslist = MembershipPlan.objects.get(id  = id)
    plans = PlanForm(instance=planslist)
    if request.method =="POST":
        plans = PlanForm(request.POST,instance=planslist)
        if plans.is_valid():
            plans.save()
            return redirect("plan_list")
    return render(request,"plansform.html",{"plans":plans})

def DeletPlanform(request,id):
    if request.method =="POST":
        form = MembershipPlan.objects.get(id  = id)
        form.delete()
        return redirect("plan_list")
    else:
        return redirect("plan_list")




def home5(request):
    trainer=   Trainer.objects.all()
    return render(request,"Trainer_list.html",{"trainers":trainer})

def TrainerForms(request):
    form =TrainerForm()
    if request.method =="POST":
        form =TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Trainer_list")
    return render(request,"trainerForm.html",{"form":form})

def TrainerUpdate(request,id):
    trainer = Trainer.objects.get(id =id)
    form =TrainerForm(instance=trainer)
    if request.method =="POST":
        form =TrainerForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
            return redirect("Trainer_list")
    return render(request,"trainerForm.html",{"form":form})

def Delettrainerform(request,id):
    if request.method =="POST":
        T_form = Trainer.objects.get(id=id)
        T_form.delete()
        return redirect("Trainer_list")
    else:
        return redirect("Trainer_list")





