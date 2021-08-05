from django.urls import path
import ex08.views

urlpatterns = [
    path('init/', ex08.views.init, name='init'),
    path('populate/', ex08.views.populate, name='populate'),
	path('display/', ex08.views.display, name='display'),
]
