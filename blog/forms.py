from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on blog posts.
    """
    class Meta:
        """
        Django model and order of the fields to be used in the form.
        """
        model = Comment
        fields = ('content',)
