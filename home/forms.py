from .models import User, Memorandum, SpecialOrder, CommLetter, Moau, Event

from django.forms import ModelForm, ImageField, FileInput, DateTimeField, DateInput, FileField, DateField

class UserPForm(ModelForm):
    avatar = ImageField(required=False, widget=FileInput)

    class Meta:
        model = User
        fields = ['avatar']

class UserIForm(ModelForm):
    birth_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())

    class Meta:
        model = User
        fields = ['gender', 'birth_date']

class MoauForm(ModelForm):
    moau_file = FileField(required=False, widget=FileInput)
    moau_approve_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())
    moau_notarized_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())

    class Meta:
        model = Moau
        fields = ['moau_file', 'moau_type', 'moau_approve_date', 'moau_notarized_date']


class EventForm(ModelForm):
    event_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())
    attendance_file = FileField(required=False, widget=FileInput)

    class Meta:
        model = Event
        fields = ['event_date', 'attendance_file']

class MemoForm(ModelForm):
    memo_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())
    memo_file = FileField(required=False, widget=FileInput)

    class Meta:
        model = Memorandum
        fields = ['memo_date', 'memo_file']

class LetterForm(ModelForm):
    letter_file = FileField(required=False, widget=FileInput)
    letter_received_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())

    class Meta:
        model = CommLetter
        fields = ['letter_file', 'letter_received_date']

class OrderForm(ModelForm):
    so_date = DateField(required=False, input_formats=['%Y-%m-%d'], widget=DateInput())
    so_file = FileField(required=False, widget=FileInput)

    class Meta:
        model = SpecialOrder
        fields = ['so_date', 'so_for', 'so_file']

