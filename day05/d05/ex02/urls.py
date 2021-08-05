from django.urls import path
import ex02.views

urlpatterns = [
    path('init/', ex02.views.init, name='init'),
    path('populate/', ex02.views.populate, name='populate'),
    path('display/', ex02.views.display, name='display'),
]
