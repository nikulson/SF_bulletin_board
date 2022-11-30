from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView

from .filters import BulletinFilter, ReplyFilter
from .forms import BulletinForm, ReplyForm
from .models import Bulletin, Category, Reply


def home(request):
    context = {
        'bulletins': Bulletin.objects.all()
    }
    return render(request, 'bulletins/home.html', context)


class BulletinListView(ListView):
    model = Bulletin
    queryset = Bulletin.objects.all()
    template_name = "bulletins/home.html"
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


class UserBulletinListView(ListView):
    model = Bulletin
    template_name = 'bulletins/user_bulletins.html'
    context_object_name = 'bulletin_list'
    ordering = ['-created_at']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Bulletin.objects.filter(author=user).order_by('-created_at')


class BulletinDetail(DetailView):
    model = Bulletin


class BulletinCreateView(LoginRequiredMixin, CreateView):
    model = Bulletin
    fields = ['title', 'content', 'category', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForm

    def form_valid(self, form):
        form.instance.bulletin_id = self.kwargs['pk']
        form.instance.username = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class BulletinUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bulletin
    fields = ['title', 'body', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        bulletin = self.get_object()
        if self.request.user == bulletin.author:
            return True
        return False


class BulletinDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bulletin
    success_url = '/home'

    def test_func(self):
        bulletin = self.get_object()

        if self.request.user == bulletin.author:
            return True
        return False


class ReplyListView(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'bulletins/reply_list.html'
    context_object_name = 'replies'
    ordering = ['-created_at']
    paginate_by = 2
    myFilter = ReplyFilter()

    def get_queryset(self):
        user_id = self.request.user.id  # get logged-in user id because he is an author of his own posts
        return Reply.objects.filter(bulletin__author_id=user_id).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ReplyFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    model = Reply
    success_url = reverse_lazy('reply_list')
