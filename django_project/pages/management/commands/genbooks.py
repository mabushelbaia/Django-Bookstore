from django.core.management.base import BaseCommand
from pages.models import Book
import os


class Command(BaseCommand):
    help = 'Generate books'

    def handle(self, *args, **options):
        # load NotesForProfessionals.com books
        titles = [title.replace('.pdf', '') for title in os.listdir('static/NotesForProfessionals/pdfs')]
        covers = [f'{title}.png' for title in titles]
        pdfs = [f'{title}.pdf' for title in titles]
        books = zip(titles, covers, pdfs)
        # clear database
        Book.objects.all().delete()
        # create books
    
        for title, cover, pdf in books:
            Book.objects.create(title=title, cover_url=cover, pdf_url=pdf)
            print(f'Book {title} {cover} {pdf} created')
