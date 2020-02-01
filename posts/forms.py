from django import forms
from tinymce import TinyMCE
from .models import Post, Comment, Author
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 'categories',
                  'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': 4
    }))

    class Meta:
        model = Comment
        fields = ('content',)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'profession', 'about_you', 'profile_picture')


# class SignUpForm(forms.ModelForm):

#     first_name = forms.CharField(
#         max_length=30, required=True, help_text='Required')
#     last_name = forms.CharField(
#         max_length=30, required=True, help_text='Required')

#     class Meta:
#         model = Author
#         fields = ('first_name', 'last_name', 'profile_picture')
