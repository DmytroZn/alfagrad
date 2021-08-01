from django import forms

from .models import AskQuestions

class FormAskQuestions(forms.ModelForm):
    class Meta:
        model = AskQuestions
        fields = ['name', 'email', 'question']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Имя', 'class':'form-input', 'id':'', 'type':'name', 'name':"name"}),
            'email': forms.TextInput(attrs={'placeholder':'E-mail','class':'form-input', 'id':'', 'type':'email', 'name':"email", 'data-constraints':"@Email @Required" }),
            'question':forms.TextInput(attrs={'placeholder':'Вопрос/комментарий','class':'form-input', 'id':'', 'type':'question', 'name':"equestionmail" })

        }
