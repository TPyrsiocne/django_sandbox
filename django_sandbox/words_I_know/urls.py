from django.urls import include, path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name = "register"),
    path("word_list/", views.word_list, name = "word_list"),
    path("word_definition/<wrd>/",views.word_definition, name = "word_definition"),
    path("word_definition/<wrd>/toggle/",views.toggle, name = "test"),
]