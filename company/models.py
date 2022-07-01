from django.db import models

# Create your models here.
class Machine(models.Model):
	CATEGORY = (
			('تک کاربر', 'تک کاربر'),
			('کاربر گروهی', 'کاربر گروهی')
	)
	name = models.CharField(max_length= 100, null= True)
	date_enter = models.DateTimeField(null= True)
	function = models.CharField(max_length=100, null= True)
	subject = models.CharField(max_length=500, null= True)
	serial_num = models.IntegerField(null= True)
	type_user = models.CharField(max_length= 30, choices= CATEGORY, null= True)
	error=  models.CharField(max_length=100, null= True)

	def __str__(self):
		return self.name

class Job(models.Model):
	name = models.CharField(max_length= 100, null= True)
	subject = models.CharField(max_length=500, null= True )

	def __str__(self):
		return (self.name)

class Personal(models.Model):
	SEX = (
		('male', 'male'),
		('female', 'female'),
	)
	f_name = models.CharField(max_length= 100, null= True)
	l_name = models.CharField(max_length= 100, null= True)
	job = models.ForeignKey(Job, null= True, on_delete= models.SET_NULL)
	date_enter = models.DateTimeField(null= True)
	education = models.CharField(max_length= 200, null = True)
	sex = models.CharField(max_length= 30, choices= SEX,null= True)
	mobile = models.CharField(max_length= 100, null= True)
	salary = models.FloatField(max_length= 100, null= True)

	def __str__(self):
		return self.l_name

class Product(models.Model):
	CATEGORY = (
		('قاشق', 'قاشق'),
		('چنگال', 'چنگال'),
		('چاقو', 'چاقو'),
		)
	model = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=50, choices=CATEGORY, null=True)
	max_in_box = models.IntegerField(null=True)
	pirce = models.FloatField(null=True)

	def __str__(self):
		return self.model

class Nameprocess(models.Model):
	name = models.CharField(max_length= 200, blank= True, null= True)
	subject = models.CharField(max_length=500, null= True)
	timeprocess = models.FloatField(null=True)

	def __str__(self):
		return self.name


class Process(models.Model):
	STATUS = (
		('in process', 'در حال تولید'),
		('complete', 'کامل'),
		('defective', 'معیوب'),
		)
	name = models.ForeignKey(Nameprocess, blank=True, null=True, on_delete=models.SET_NULL)
#	name = models.CharField(max_length= 100, null= True)
	personal = models.ForeignKey(Personal, null=True, on_delete=models.SET_NULL)
	Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	machine = models.ForeignKey(Machine, null=True, on_delete=models.SET_NULL)
	status = models.CharField(max_length=50, choices=STATUS, null=True)
	date = models.DateTimeField(auto_now_add=True)
	number = models.IntegerField(null=True)

	def __str__(self):
		return self.name

