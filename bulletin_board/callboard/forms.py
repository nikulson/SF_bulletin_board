from django import forms
from .models import Reply, Bulletin

from django.forms import ModelForm, BooleanField


# Создаём модельную форму
class BulletinForm(ModelForm):
    check_box = BooleanField(label='Готово')

    class Meta:
        model = Bulletin
        fields = ['title', 'body', 'author', 'category', 'check_box']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["body"]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
