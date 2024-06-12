from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


from .models import Book
import os

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'



class AboutPageView(TemplateView):
    template_name = 'about.html'

class BooksView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        if self.request.user.is_authenticated:
            favorites = self.request.user.favorites.all()
        else:
            favorites = None
        context['favorites'] = favorites
        context['books'] = books
        return context
    

class LikesView(TemplateView, LoginRequiredMixin):
    # add login required

    template_name = 'likes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            favorites = self.request.user.favorites.all()
        else:
            favorites = None
        context['favorites'] = favorites
        return context

@login_required
def add_to_favorites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.favorites.add(book)
    # get back to the previous page
    print(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') if reverse('login') not in request.META.get('HTTP_REFERER') else reverse('home'))

@login_required
def remove_from_favorites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.favorites.remove(book)
    # get back to the previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




