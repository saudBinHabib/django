from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))

    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'saud' in title:
            return title
        else:
            raise forms.ValidationError('This is not a proper title.')


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your Description',
                'class': 'new-class-name two',
                'id': 'my-id-for-textarea',
                'rows': 3,
                'cols': 20,
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
