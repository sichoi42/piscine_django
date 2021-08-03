from django.urls import path
import ex00.views

urlpatterns = [
    path('', ex00.views.index, name='index'),
]
