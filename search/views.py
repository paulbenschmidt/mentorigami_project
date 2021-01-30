from django.shortcuts import render

def search_results(request):
    return render(request, 'search_results.html')
