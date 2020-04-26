from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]
        # title = forms.CharField(max_length=50)
        # content = forms.CharField()
        # active = forms.BooleanField()
