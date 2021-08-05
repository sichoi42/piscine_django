from django.urls import path
import ex04.views

urlpatterns = [
	path('init/', ex04.views.init, name='init'),
	path('populate/', ex04.views.populate, name='populate'),
	path('display/', ex04.views.display, name='display'),
	path('remove/', ex04.views.remove, name='remove'),
]
