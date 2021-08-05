from django.urls import path
import ex06.views

urlpatterns = [
    path('init/', ex06.views.init, name='init'),
    path('populate/', ex06.views.populate, name='populate'),
    path('display/', ex06.views.display, name='display'),
	path('update/', ex06.views.update, name='update'),
]
