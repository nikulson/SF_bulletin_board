from django.shortcuts import render
from django.views.generic import ListView
from models import Bulletin


def home(request):
    context = {
        'bulletins': Bulletin.objects.all()
    }
    return render(request, 'bulletin_board/home.html', context)


class BulletinListView(ListView):
    model = Bulletin
    ordering = '-created_at'
    template_name = 'bulletin_board/home.html'
    context_object_name = 'bulletins_0'
    paginate_by = 2




