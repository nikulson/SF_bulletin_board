from django.forms import DateInput
from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from .models import Bulletin


# создаём фильтр
class BulletinFilter(FilterSet):
    title = CharFilter('title',
                       label='Заголовок содержит:',
                       lookup_expr='icontains',
                       )

    body = CharFilter('body',
                      label='Текст содержит:',
                      lookup_expr='icontains',
                      )

    author = CharFilter(field_name='author',
                        label='Автор:',
                        lookup_expr='exact',
                        )
    created_at = DateFilter(
        field_name='created_at',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='gt',
        label='Даты позже'
    )

    class Meta:
        model = Bulletin
        fields = []
