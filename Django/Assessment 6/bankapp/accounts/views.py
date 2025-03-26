from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Account, Transaction
from .forms import CustomerForm, AccountForm, TransactionForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    accounts = customer.accounts.all()
    return render(request, 'accounts/customer_detail.html', {
        'customer': customer,
        'accounts': accounts
    })

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = account.transactions.all().order_by('-created_at')
    return render(request, 'accounts/account_detail.html', {
        'account': account,
        'transactions': transactions
    })

def create_transaction(request, account_pk):
    account = get_object_or_404(Account, pk=account_pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = account
            transaction.save()
            return redirect('account_detail', pk=account.pk)
    else:
        form = TransactionForm()
    return render(request, 'accounts/transaction_form.html', {
        'form': form,
        'account': account
    })
