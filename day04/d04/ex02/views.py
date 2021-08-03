import logging, logging.handlers
from django.shortcuts import redirect, render
from django.conf import settings
from . import forms

def submit(request):
	logger = logging.getLogger('django.request')
	form = forms.Log(request.POST)
	if form.is_valid():
		logger.info(form.cleaned_data['history'])
		return redirect('/ex02')
	f = open(settings.LOG_FILE, 'r')
	logs = [line for line in f.readlines()]
	context = {'form': forms.Log(), 'logs': logs,}
	return render(request, 'form.html', context)
