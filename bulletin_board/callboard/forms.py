from django import forms
from .models import Reply


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ["body"]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
