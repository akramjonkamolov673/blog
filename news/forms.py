from django import forms
from news.models import PostModel,Comment

class PostModelForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':4,'style':'resize:none;'}))
    class Meta:
        model=PostModel
        fields=('title','content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=('title','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)