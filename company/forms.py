from django.forms import ModelForm
from .models import Process,User,Machine

class processForm(ModelForm):
	class Meta:
		model = Process
		fields = '__all__'

class userForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class machineForm(ModelForm):
	class Meta:
		model = Machine
		fields = '__all__'