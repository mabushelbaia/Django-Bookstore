from django.urls import path
from .views import HomePageView, BooksView, LikesView, add_to_favorites, remove_from_favorites

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("notebooks/", BooksView.as_view(), name="notebooks"),
    path('notebooks/add_to_favorites/<int:book_id>/', add_to_favorites, name='add_to_favorites'),
    path('notebooks/remove_from_favorites/<int:book_id>/', remove_from_favorites, name='remove_from_favorites'),
    path("bookmarks/", LikesView.as_view(), name="likes"),
]
