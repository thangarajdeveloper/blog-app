from django import forms
from .models import BlogModel


class CommentForm(forms.Form):
    # This form used is for adding and view the comments
    your_name = forms.CharField(max_length=20)
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"


class SearchForm(forms.Form):
    # This form used is for search blogs using title
    title = forms.CharField(max_length=20)


class BlogForm(forms.ModelForm):
    # This form used is for add, update blogs
    class Meta:
        model = BlogModel
        fields = ('id', 'blog_title', 'blog')
