from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.core import validators
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()

class DispatcherLoginForm(forms.Form):
    email = forms.CharField(
        label='Введите email:',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Введите пароль:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого диспетчера не существует в системе!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль!')

            authenticate(email=email, password=password)

        return super(DispatcherLoginForm, self).clean(*args, **kwargs)


class DispatcherRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label="Имя:",
        validators=[validators.RegexValidator(regex='^[А-Я][а-яєі]')],
        error_messages={'invalid': 'Сожержимое данного поля должно быть кириллицей!'},
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    phone_number = PhoneNumberField(
        label='Введите номер:',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='Email-адрес:',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        label='Введите пароль:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password2 = forms.CharField(
        label='Введите пароль ещё раз:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')

        return data['password2']