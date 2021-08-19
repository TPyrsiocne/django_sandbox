from django.shortcuts import render, HttpResponse

def dashboard(request):
    return render(request, "words_I_know/dashboard.html")