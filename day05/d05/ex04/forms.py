from django import forms

class Remove(forms.Form):
	title = forms.ChoiceField(choices=())

	def __init__(self, choices, *args, **kwargs):
		super(Remove, self).__init__(*args, **kwargs)
		self.fields['title'].choices = choices
