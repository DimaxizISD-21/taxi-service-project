from django import forms
from django.core import validators
from phonenumber_field.formfields import PhoneNumberField
from flatpickr import TimePickerInput

from taxi.models import TaxiOrder


class TaxiOrderForm(forms.ModelForm):
    client_name = forms.CharField(
        label='Введите имя:',
        validators=[validators.RegexValidator(regex='^[А-Я][а-яєі]')],
        error_messages={'invalid': 'Сожержимое данного поля должно быть кириллицей!'},
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    phone_number = PhoneNumberField(
        label='Введите номер:',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    address = forms.CharField(
        label='Укажите адрес:',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    desired_time = forms.TimeField(
        label='Укажите желаемое время:',
        widget=TimePickerInput(),
        required=True
    )

    class Meta:
        model = TaxiOrder
        fields = ('client_name', 'phone_number', 'address', 'desired_time',)
