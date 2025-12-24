# accountant/forms.py
from django import forms
from .models import Account, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'type', 'amount']
