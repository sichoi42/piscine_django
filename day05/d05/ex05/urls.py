from django.urls import path
import ex05.views

urlpatterns = [
	path('populate/', ex05.views.populate, name='populate'),
	path('display/', ex05.views.display, name='display'),
	path('remove/', ex05.views.remove, name='remove'),
]
