from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your Title'
            }
        )
    )

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'cols': 50,
                'rows': 15,
                'placeholder': 'Enter your Content'
            }
        )
    )

    class Meta:
        model = Article
        fields = ['title', 'content', 'active']