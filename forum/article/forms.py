from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    """
    form校验表单输入
    """
    #title = forms.CharField(label="标题", max_length=20)

    #content = forms.CharField(label="内容", max_length=100)
    class Meta:
        model = Article
        fields = ["title", "content"]
