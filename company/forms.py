from django.forms import ModelForm
from .models import Process, Personal, Machine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class processForm(ModelForm):
	class Meta:
		model = Process
		fields = '__all__'

class personalForm(ModelForm):
	class Meta:
		model = Personal
		fields = '__all__'

class machineForm(ModelForm):
	class Meta:
		model = Machine
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']