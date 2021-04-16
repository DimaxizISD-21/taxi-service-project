from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

class DispatcherLoginForm(forms.Form):
    email = forms.CharField(
        label='Введите email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого диспетчера не существует в системе!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль!')

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Этот диспетчер сейчас не в сети!')

        return super(DispatcherLoginForm, self).clean(*args, **kwargs)


class DispatcherRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label="Имя:",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    phone_number = forms.CharField(
        label="Номер телефону",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
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