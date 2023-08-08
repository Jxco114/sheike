from django import forms

from .models import New_message

class Clientmsg(forms.ModelForm):
    class Meta:
        model = New_message
        fields = '__all__'