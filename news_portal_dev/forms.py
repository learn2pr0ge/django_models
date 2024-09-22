from django import forms
from .models import Post


class PostForm(forms.ModelForm):


    class Meta:
        model = Post

        # Можно подставить fields = "__all__"
        fields = ['author', 'category','title', 'content']

