from django import forms

from .models import CourseModel


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.lower() == 'abc':
            raise forms.ValidationError("this is not a valid form")
        return title