from django import forms
from phonenumber_field.formfields import PhoneNumberField
from flatpickr import TimePickerInput

from taxi.models import TaxiOrder, TaxiAuto


class TaxiOrderForm(forms.Form):
    client_name = forms.CharField(
        label='Введите имя:',
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
        # widget=forms.TextInput(attrs={'class': 'form-control'}),
        # widget=forms.TimeInput(format='%H:%M'),
        widget=TimePickerInput(),
        required=True
    )
    taxi_auto = forms.ModelChoiceField(
        queryset=TaxiAuto.objects.filter(taxi_status='free'),
        label='Список доступных авто:',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = TaxiOrder
        fields = ('client_name', 'phone_number', 'address', 'desired_time', 'taxi_auto',)
