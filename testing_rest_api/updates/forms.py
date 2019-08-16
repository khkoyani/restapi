from django import forms
from .models import Update

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ['content', 'image', 'user']

    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content', None)
        print(self.cleaned_data)
        if content == '':
            content = None
        image = self.cleaned_data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('Data must include content or image', code='invalid')
        return super(UpdateForm, self).clean(*args, **kwargs)