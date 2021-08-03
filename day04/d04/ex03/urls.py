from django.urls import path
import ex03.views

urlpatterns = [
	path('', ex03.views.coloring, name='coloring'),
]
