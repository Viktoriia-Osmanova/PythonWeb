from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote

def authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors_list': authors_list})

@login_required
def add_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        Author.objects.create(name=name)
        return redirect('authors')
    return render(request, 'add_author.html')

def quotes(request):
    quotes_list = Quote.objects.all()
    return render(request, 'quotes.html', {'quotes_list': quotes_list})

@login_required
def add_quote(request):
    if request.method == 'POST':
        text = request.POST['text']
        author_id = request.POST['author']
        author = Author.objects.get(pk=author_id)
        Quote.objects.create(text=text, author=author)
        return redirect('quotes')
    
    authors_list = Author.objects.all()
    return render(request, 'add_quote.html', {'authors_list': authors_list})

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
