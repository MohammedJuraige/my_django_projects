from django import forms
from .models import Comment,Page
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']



class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']


class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'