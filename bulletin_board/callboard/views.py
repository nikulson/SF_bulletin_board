from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView

from .models import Bulletin


class BulletinListView(View):
    """Список объявлений"""

    def get(self, request):
        bulletins = Bulletin.objects.all()
        return render(request, "bulletins/bulletin_list.html", {"bulletin_list": bulletins})


