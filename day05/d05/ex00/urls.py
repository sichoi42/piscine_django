from django.urls import path
import ex00.views

urlpatterns = [
    path('init/', ex00.views.init, name='init'),
]
