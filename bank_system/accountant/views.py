
# from django.shortcuts import render, redirect
# from .forms import AccountForm, TransactionForm

# def create_account(request):
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             account = form.save(commit=False)
#             account.owner = request.user
#             account.save()
#             return redirect('accountant:dashboard')
#     else:
#         form = AccountForm()
#     return render(request, 'accountant/create_account.html', {'form': form})

# def transaction(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accountant:dashboard')
#     else:
#         form = TransactionForm()
#     return render(request, 'accountant/transaction.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm

def dashboard(request):

    accounts = Account.objects.filter(owner=request.user)
    return render(request, 'accountant/index.html')


def create_account(request):
    """
    Show a form to create a new account. On POST, save and redirect to dashboard.
    URL: /accountant/create-account/
    Template: accountant/create_account.html
    """
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            acc = form.save(commit=False)
            acc.owner = request.user
            acc.save()
            return redirect('accountant:dashboard')
    else:
        form = AccountForm()
    return render(request, 'accountant/create_account.html', {'form': form})


def transaction(request):
    """
    Show a form to make a deposit or withdrawal. On POST, record it and redirect.
    URL: /accountant/transaction/
    Template: accountant/transaction.html
    """
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()  # Updates Account balance through model logic
            return redirect('accountant:dashboard')
    else:
        form = TransactionForm()
    return render(request, 'accountant/transaction.html', {'form': form})
