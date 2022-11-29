from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView

from .filters import BulletinFilter
from .forms import BulletinForm
from .models import Bulletin, Category


# class BulletinListView(View):
#     """Список объявлений"""
#
#     def get(self, request):
#         bulletins = Bulletin.objects.all()
#         return render(request, "bulletins/bulletin_list.html", {"bulletin_list": bulletins})

class BulletinListView(ListView):
    model = Bulletin
    queryset = Bulletin.objects.all()
    template_name = "bulletins/bulletin_list.html"
    context_object_name = 'bulletin_list'
    ordering = ['-created_at']
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BulletinFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        context['filter'] = BulletinFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['author'] = Bulletin.author
        context['form'] = BulletinForm()
        context['filterset'] = self.filterset
        return context





