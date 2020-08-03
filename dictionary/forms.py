from django import forms
from .models import Dictionary
from django.core.exceptions import ValidationError

class add_word(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ['word', 'definition']

class input_form(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ['word']
    def validate_word(self):
        word =self.cleaned_data['word']
        if len(word) > 100:
            raise ValidationError("The length of the word is 100 characters !")
        return word
