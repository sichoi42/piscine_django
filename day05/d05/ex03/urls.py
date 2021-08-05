from django.urls import path
import ex03.views

urlpatterns = [
	path('populate/', ex03.views.populate, name='populate'),
	path('display/', ex03.views.display, name='display'),
]
