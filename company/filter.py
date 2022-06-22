import django_filters

from .models import *

class processfilter(django_filters.FilterSet):
	class Meta:
		model : Process
		fields :'__all__'