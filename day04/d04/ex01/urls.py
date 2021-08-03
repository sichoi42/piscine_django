from django.urls import path
import ex01.views

urlpatterns = [
    path('django/', ex01.views.django, name='django'),
    path('display/', ex01.views.display, name='display'),
    path('templates/', ex01.views.templates, name='templates'),
]
