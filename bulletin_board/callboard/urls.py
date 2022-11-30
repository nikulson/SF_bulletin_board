from django.urls import path
from . import views
from .views import BulletinListView, UserBulletinListView, ReplyListView

urlpatterns = [
    path('', BulletinListView.as_view(), name='home'),
    path('user/<str:username>', UserBulletinListView.as_view(), name='user-posts'),
    path('home/replies', ReplyListView.as_view(), name='reply_list'),

]
