from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Book

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

    try:
        book_count = Book.objects.count()
    except Exception as e:
        print(e)
        # Handle the exception appropriately, such as logging the error and setting book_count to 0
        book_count = 0
    try:
        user_count = get_user_model().objects.count()
    except Exception as e:
        print(e)
        # Handle the exception appropriately, such as logging the error and setting user_count to 0
        user_count = 0
    context = {
        'book_count': book_count,
        'user_count': user_count,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_count'] = self.book_count
        context['user_count'] = self.user_count
        return context



class BooksView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        # remove "NotesForProfessionals" from all books titles
        for book in books:
            book.title = book.title.replace("NotesForProfessionals", "")

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
            for book in favorites:
                book.title = book.title.replace("NotesForProfessionals", "")
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
