# accountant/models.py
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.owner.username}): {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        self.balance -= amount
        self.save()


class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=1, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Adjust the account balance when a transaction is created
        if not self.pk:  # new transaction
            if self.type == 'D':
                self.account.deposit(self.amount)
            else:
                self.account.withdraw(self.amount)
        super().save(*args, **kwargs)

