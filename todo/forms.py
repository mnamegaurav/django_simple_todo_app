from django import forms
from .models import ToDo

class ToDoForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(
                                                attrs={
                                                    'class':'form-control',
                                                    'placeholder':'Enter todo',
                                                    })
                                                )



	# class Meta:
	# 	model = ToDo

	# 	fields = ('text','complete',)

	# 	widgets = {'text': TextInput(attrs={'class':'form-control',
	# 		'placeholder':'Enter todo',
	# 		'aria-label':'Todo',
	# 		'aria-describedby':'add-btn',}),}