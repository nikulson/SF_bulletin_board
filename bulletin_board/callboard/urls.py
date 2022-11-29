from django.urls import path
from . import views
from .views import BulletinListView

urlpatterns = [
    path('', BulletinListView.as_view(), name='home'),

]
