from django.urls import path, reverse
from django.conf import urls
from . import views

urlpatterns = [
	
	path("", views.dashboard, name= "home"),
	path("update_process/<str:pk>/", views.updateprocess, name = 'update_process'),
	path("userenter/", views.userenter, name="userenter"),
	path("update_user/<str:pk>/", views.updateuser, name="update_user"),
	path("enterprocess/", views.enterProcess, name="enterprocess"),
	path("user_views/<str:pk>/", views.userviews, name="user_views"),#jahate namayeshe user ha ke be template edituser.html mifreste
	path("delete_process/<str:pk>/", views.deleteProcess, name = 'delete_process'),	
	path("chart/", views.chart, name="chart"),
	path("machine_view/<str:pk>/", views.machineview, name="machine_view"),
	path("machine_enter/", views.machineenter, name="machine_enter"),
	path("update_machine/<str:pk>/", views.updatemachine, name="update_machine"),
]