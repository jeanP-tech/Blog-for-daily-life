from django import forms
from .models import Post
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

    secret = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label='',
        help_text='secret',
        required='False'
    )

    class Meta:
        model = Post
        fields = ['title', 'text']
