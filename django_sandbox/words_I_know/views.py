from django.contrib.auth import login
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from words_I_know.models import Word

def dashboard(request):
    return render(request, "words_I_know/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(request, 'words_I_know/register.html', {'form' : UserCreationForm})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            return render(request, 'words_I_know/invalid_username.html')


def word_list(request):
    return render(request, 'words_I_know/word_list.html', { 'word_list' : Word.objects.all()})