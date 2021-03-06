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
            return render(request, 'words_I_know/invalid_registration.html')


def word_list(request):
    return render(request, 'words_I_know/word_list.html', { 'word_list' : Word.objects.order_by('word_txt')})

def word_definition(request, wrd):
    this_word = Word.objects.filter(word_txt = wrd).first()
    return render(request, 'words_I_know/word_definition.html',{'this_word' : this_word})

def toggle(request, wrd):
    current_user = request.user
    word_to_toggle = Word.objects.get(word_txt = wrd)

    if current_user.is_authenticated:
        if current_user in word_to_toggle.known_by.all():
            word_to_toggle.known_by.remove(current_user)
        else:
            word_to_toggle.known_by.add(current_user)
    else:
        return redirect("/words_I_know/dashboard.html")

    return redirect("/words_I_know/word_definition/" + wrd +"/")
