from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from .filter import *

# Create your views here.
def dashboard(request):
	process = Process.objects.all()
	product = Product.objects.all()
	user = User.objects.all()
	machine = Machine.objects.all()
	total_process = process.count()
	total_user = user.count()
	total_machine = machine.count()

	context = {
		'process' : process,
		'product' : product,
		'user' : user,
		'machine' : machine,
		'total_user' : total_user,
		'total_process' : total_process,
		'total_machine' : total_machine,
	}

	return render(request, "company/dashboard.html", context)

def updateprocess (request, pk):
	process = Process.objects.get(id = pk)
	form = processForm(instance=process)
	if request.method == 'POST':
		form = processForm(request.POST, instance=process)
		if form.is_valid():
			form.save()
			return redirect('/enterprocess/')
	context = {'form' : form}

	def __str__(self):
		return str(self.id)	
	return render(request, "company/process.html", context)

def enterProcess (request):
	process = Process.objects.all()
	form = processForm()
	if request.method == 'POST':
		form = processForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form' : form,
		'process' : process,
		}
	
	return render(request, "company/process.html", context)

def deleteProcess (request, pk):
	process = Process.objects.get(id = pk)
	if request.method == 'POST':
		process.delete()
		return redirect('/')
	context = {'item' : process}

	return render (request, "company/deleteProcess.html" , context)

def userviews (request, pk):

	user = User.objects.get(id = pk)
	process = Process.objects.all()
	#total_process = process.count(user.id)
#	form = userForm(instance = user)
#	if request.method == 'POST':
#		form = userForm(request.POST, instance=user)
#	context = {'form' : form}

	context = {
		'user' : user,
		'process' : process,
	}

	return render(request, "company/edituser.html", context)

def userenter (request):
	user = User.objects.all()
	form = userForm()
	if request.method == 'POST':
		form = userForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form' : form,
		'user' : user,
		}

	return render(request, "company/user.html", context)

def updateuser (request, pk):
	user = User.objects.get(id = pk)
	form = userForm(instance= user)
	if request.method == 'POST':
		form = userForm(request.POST, instance= user)
		if form.is_valid():
			form.save()
	context = {'form' : form}

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
	context={
		'lable' : lable,
		'data' : data,
	}

	return render (request, "company/chart.html", context)

def machineview (request, pk):

	machine = Machine.objects.get(id = pk)
	process = Process.objects.all()
	context = {
		'machine' : machine,
		'process' : process,
	}

	return render(request, "company/machine.html", context)

def machineenter (request):
	machine = Machine.objects.all()
	form = machineForm()
	if request.method == 'POST':
		form = machineForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	context = {	
		'form' : form,
		'machine' : machine,
	}
	return render(request, "company/machine.html", context)

def updatemachine (request, pk):
	machine = Machine.objects.get(id = pk)
	form = machineForm(instance=machine)
	if request.method == 'POST':
		form = machineForm(request.POST, instance=machine)
		if form.is_valid():
			form.save()
	context = {'form' : form}

	def __str__(self):
		return str(self.id)	
	return render(request, "company/machineedit.html", context)	