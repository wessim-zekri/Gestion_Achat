from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.models import Group
from django import forms
from .models import Demande, Fournisseur, Employé, Commande, Piece, Demande_Validée, Csv


class DemandeForm(ModelForm):
    class Meta:
        model = Demande
        fields = '__all__'

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'group']

class EmployéForm(ModelForm):
    class Meta:
        model = Employé
        fields = '__all__'

class DemandeValForm(ModelForm):
    class Meta:
        model = Demande_Validée
        fields = '__all__'

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class PieceForm(ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ['file_name']