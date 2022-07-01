from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, reverse
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filter import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth

# Create your views here.
def register(request):
    if request.user.is_authenticate:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"ثبت نام شما با موفقیت انجام شد" + user)

                return redirect('login')


        context = {'form': form}
        return render(request, 'company/register.html', context)

def loginpage(request):
    if request.user.is_authenticate:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'نام کاربری یا رمز عبور اشتباه است')

        context = {}
        return render(request, 'company/login.html', context)

def logout(request):
    context = {}
    return render(request, 'login.html', context)
@login_required(login_url='login')
def dashboard(request):
    process = Process.objects.all()
    product = Product.objects.all()
    personal = Personal.objects.all()
    machine = Machine.objects.all()
    temp = 0
    for p in process:
        if p.status == "in process":
            temp += p.number
    temp1 = 0
    for p in process:
        if p.status == "complete":
            temp1 += p.number
    temp2 = 0
    for p in process:
        if p.status == "defective":
            temp2 += p.number
    total_in_process = temp
    total_complete = temp1
    total_defective = temp2

    context = {
        'process': process,
        'product': product,
        'personal': personal,
        'machine': machine,
        'total_complete': total_complete,
        'total_in_process': total_in_process,
        'total_defective': total_defective,
    }

    return render(request, "company/dashboard.html", context)


def updateprocess(request, pk):
    process = Process.objects.get(id=pk)
    form = processForm(instance=process)

    if request.method == 'POST':
        form = processForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('/enterprocess/')
    context = {'form': form}

    def __str__(self):
        return str(self.id)

    return render(request, "company/process.html", context)


def EnterProcess(request):
    process = Process.objects.all()

    myfilter = processfilter()

    form = processForm()
    if request.method == 'POST':
        form = processForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'process': process,
        'myfilter': myfilter,
    }

    return render(request, "company/process.html", context)


def deleteProcess(request, pk):
    process = Process.objects.get(id=pk)
    if request.method == 'POST':
        process.delete()
        return redirect('/')
    context = {'item': process}

    return render(request, "company/deleteProcess.html", context)


def userviews(request, pk):
    personal = Personal.objects.get(id=pk)
    process = Process.objects.all()
    # total_process = process.count(user.id)
    #	form = userForm(instance = user)
    #	if request.method == 'POST':
    #		form = userForm(request.POST, instance=user)
    #	context = {'form' : form}

    context = {
        'personal': personal,
        'process': process,
    }

    return render(request, "company/edituser.html", context)


def userenter(request):
    personal = Personal.objects.all()
    form = personalForm()
    if request.method == 'POST':
        form = personalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'personal': personal,
    }

    return render(request, "company/user.html", context)


def updateuser(request, pk):
    personal = Personal.objects.get(id=pk)
    form = personalForm(instance=personal)
    if request.method == 'POST':
        form = personalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
    context = {'form': form}

    def __str__(self):
        return str(self.id)

    return render(request, "company/edituser.html", context)


def chart(request):
    lable = []
    data = []

    queryset = Process.objects.order_by('number')[:5]
    for pro in queryset:
        lable.append(pro.name)
        data.append(pro.number)
    context = {
        'lable': lable,
        'data': data,
    }

    return render(request, "company/chart.html", context)


def machineview(request, pk):
    machine = Machine.objects.get(id=pk)
    process = Process.objects.all()
    context = {
        'machine': machine,
        'process': process,
    }

    return render(request, "company/machine.html", context)


def machineenter(request):
    machine = Machine.objects.all()
    form = machineForm()
    if request.method == 'POST':
        form = machineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        'machine': machine,
    }
    return render(request, "company/machine.html", context)


def updatemachine(request, pk):
    machine = Machine.objects.get(id=pk)
    form = machineForm(instance=machine)
    if request.method == 'POST':
        form = machineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
    context = {'form': form}

    def __str__(self):
        return str(self.id)

    return render(request, "company/machineedit.html", context)
