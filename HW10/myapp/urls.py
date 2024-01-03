from django.urls import path
from .views import authors, add_author, quotes, add_quote

urlpatterns = [
    path('authors/', authors, name='authors'),
    path('add_author/', add_author, name='add_author'),
    path('quotes/', quotes, name='quotes'),
    path('add_quote/', add_quote, name='add_quote'),
]
