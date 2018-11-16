from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your Title'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email'
            }
        )
    )
    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'class-one class-two',
                'id': 'id-for-description',
                'placeholder': 'Provide a Description',
                'cols': 25,
                'rows': 10
            }
        )
    )
    price = forms.DecimalField(initial=12.55)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if 'Pro' not in title:
    #         raise forms.ValidationError('This is not a valid title')
    #     if 'new' not in title:
    #         raise forms.ValidationError('This is not a valid title')
    #     return title
    #
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not email.endswith('edu'):
    #         raise forms.ValidationError('Provide a valid email')
    #     return email


class ProductRawForm(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'class-one class-two',
                'id': 'id-for-description',
                'placeholder': 'Provide a Description',
                'cols': 25,
                'rows': 10
            }
        )
    )
    price = forms.DecimalField(initial=12.55)
