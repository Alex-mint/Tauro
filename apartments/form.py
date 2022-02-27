import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import BookingDate, Apartment, PageMessage
from django.utils.translation import gettext_lazy as _

from datetime import timedelta


class AddReservationForm(forms.Form):
    check_in = forms.DateField(label=_('Entrada'),
                               widget=forms.TextInput(attrs={'type': 'date'}))
    check_out = forms.DateField(label=_('Salida'),
                                widget=forms.TextInput(attrs={'type': 'date'}))

    def clean(self):
        check_out = self.cleaned_data['check_out']
        check_in = self.cleaned_data['check_in']

        if (check_in - datetime.date.today()).days < 3:
            text = PageMessage.objects.get(title='2_days')
            raise forms.ValidationError(text.text)
        reserva_days = (check_out - check_in).days
        if reserva_days < 7:
            text = PageMessage.objects.get(title='minimo_noches')
            raise forms.ValidationError(text.text)
        return self.cleaned_data


class AddBookingForm(forms.Form):
    first_name = forms.CharField(label=_('Nombre'), widget=forms.TextInput(
        attrs={'class': 'form-field'}))
    last_name = forms.CharField(label=_('Apellidos'), widget=forms.TextInput(
        attrs={'class': 'form-field'}))
    phone = forms.CharField(label=_('Teléfono'), widget=forms.TextInput(
        attrs={'class': 'form-field'}))
    # guests = forms.ImageField(label='Huéspedes', widget=forms.TextInput(
    #     attrs={'class': 'form-field'}))
    comment = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 5, 'class': 'form-field'}),
                              label=_('Comentario'))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('Usuario'), widget=forms.TextInput(
        attrs={'class': 'form-field'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-field'}))
    password1 = forms.CharField(label=_('Contraseña'), widget=forms.PasswordInput(
        attrs={'class': 'form-field'}))
    password2 = forms.CharField(label=_('Rep. contraseña'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-field'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=_('Usuario'), widget=forms.TextInput(
        attrs={'class': 'form-field'}))
    password = forms.CharField(label=_('Contraseña'), widget=forms.PasswordInput(
        attrs={'class': 'form-field'}))
