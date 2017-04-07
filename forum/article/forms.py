from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(label="标题", max_length=20)  # 默认都是必须字段,不必须字段需加required=False
    # content = forms.CharField(label="内容", max_length=1000)
    # 使用forms.ModelForm代替forms.Form
    class Meta:
        model = Article
        fields = ["title", "content"]
