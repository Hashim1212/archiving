import django_filters
from .models import Moau, Event, Memorandum, CommLetter, SpecialOrder
from django import forms

class MoauFilter(django_filters.FilterSet):

    moau_approve_date = django_filters.DateFilter(lookup_expr='contains')

    class Meta:
        model = Moau
        fields = {
            'moau_title': ['icontains'],
            'moau_type': ['exact']
        }

class EventFilter(django_filters.FilterSet):
    event_date = django_filters.DateFilter(lookup_expr='contains')

    class Meta:
        model = Event
        fields = {
            'event_name': ['icontains'],
            'event_agenda': ['icontains'],
            'event_venue': ['icontains'],
            'impl_agency': ['icontains'],
        }


class MemorandumFilter(django_filters.FilterSet):
    memo_date = django_filters.DateFilter(lookup_expr='contains')

    class Meta:
        model = Memorandum
        fields = {
            'memo_subject': ['icontains'],
            'memo_content': ['icontains'],
            'memo_recomm_by': ['icontains'],
            'memo_approved_by': ['icontains'],
        }

class CommLetterFilter(django_filters.FilterSet):

    class Meta:
        model = CommLetter
        fields = {
            'letter_subject': ['icontains'],
            'letter_to': ['icontains'],
            'letter_from': ['icontains'],
            'letter_noted_by': ['icontains'],
            'letter_approved_by': ['icontains'],
        }


class SpecOrderFilter(django_filters.FilterSet):
    so_date = django_filters.DateFilter(lookup_expr='contains')

    class Meta:
        model = SpecialOrder
        fields = {
            'so_subject': ['icontains'],
            'so_content': ['icontains'],
            'so_for': ['icontains'],
            'so_signedby': ['icontains'],
        }