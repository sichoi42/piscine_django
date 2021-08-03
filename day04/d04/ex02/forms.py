from django import forms

class Log(forms.Form):
	history = forms.CharField(label="history")


