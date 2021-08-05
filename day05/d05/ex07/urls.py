from django.urls import path
import ex07.views

urlpatterns = [
	path('populate/', ex07.views.populate, name='populate'),
	path('display/', ex07.views.display, name='display'),
	path('update/', ex07.views.update, name='update'),
]
