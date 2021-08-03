from django.urls import path
import ex02.views

urlpatterns = [
	path('', ex02.views.submit, name='submit'),
]
