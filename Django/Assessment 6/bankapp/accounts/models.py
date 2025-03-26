from django.db import models
from django.core.validators import MinValueValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
        ('fixed', 'Fixed Deposit'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_type} Account - {self.customer}"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('transfer', 'Transfer'),
    )
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.created_at}"

    def save(self, *args, **kwargs):
        # Update account balance when transaction is saved
        if not self.pk:  # Only for new transactions
            if self.transaction_type == 'deposit':
                self.account.balance += self.amount
            elif self.transaction_type == 'withdrawal':
                self.account.balance -= self.amount
            self.account.save()
        super().save(*args, **kwargs)
