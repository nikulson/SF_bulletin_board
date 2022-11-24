from django.contrib import admin

from .models import Bulletin, Category, Reply

admin.site.register(Bulletin)
admin.site.register(Category)
admin.site.register(Reply)
