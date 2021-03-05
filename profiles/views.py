from django.shortcuts import render

def settings(request):
    return render(request, 'profiles/settings.html')

def sign_in(request):
    return render(request, 'profiles/sign_in.html')
