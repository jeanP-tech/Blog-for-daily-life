from django import forms
from .models import Post, Paint
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': 'Enter title here.',}),
        label=''
        )

    text = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label=''
        )

    class Meta:
        model = Post
        fields = ['title', 'text']


class PaintForm(forms.ModelForm):

    title = forms.CharField()
    image = forms.CharField()
