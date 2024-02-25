from django.shortcuts import render

# taxapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 0.15  # 15%

def default_view(request):
    return render(request, 'taxapp/default.html')

def calculate_tax(request, price):
    total = float(price) * (1 + tax_rate)
    return HttpResponse(f'Total Price with {tax_rate*100}% Tax: ${total:.2f}')

def tax_rate_view(request):
    return render(request, 'taxapp/taxrate.html', {'tax_rate': tax_rate})
