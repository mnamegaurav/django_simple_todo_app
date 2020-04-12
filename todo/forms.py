from django.forms import ModelForm,  TextInput
from .models import ToDo

class ToDoForm(ModelForm):
	class Meta:
		model = ToDo

		fields = ('text','complete',)

		widgets = {'text': TextInput(attrs={'class':'form-control',
			'placeholder':'Enter todo',
			'aria-label':'Todo',
			'aria-describedby':'add-btn',}),}