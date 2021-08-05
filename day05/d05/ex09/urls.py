from django.urls import path
import ex09.views

urlpatterns = [
	path('populate/', ex09.views.populate, name='populate'),
	#path('display/', ex09.views.display, name='display'),
]
