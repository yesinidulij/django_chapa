from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    amount = 500

    ctx = {
        'amount':amount
    }
    return render(request, 'chapa/chapa.html', ctx)

def nextpage(request):
    return render(request, 'chapa/next.html')