from django import forms
from .models import User, Reserva

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kw):
        # self.request = kw.pop('request', None)
        super(RegisterForm, self).__init__(*args, **kw)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'matricula', 'tipo')

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('turma', 'data', 'hora_inicial', 'hora_final')
        widgets = {
            'data': DateInput()
        }
        