from .models import Status
from django import forms

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['user', 'content', 'image']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 300:
            raise forms.ValidationError('Only allowed to have a maximum of 300 characters')
        return content

    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content', None)
        if content == '':
            content = None
        image = self.cleaned_data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('Data must include content or image', code='invalid')
        return super(StatusForm, self).clean(*args, **kwargs)