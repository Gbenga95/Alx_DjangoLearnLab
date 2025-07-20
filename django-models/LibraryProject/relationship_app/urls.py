# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views
# from .views import LibrarianView
# from .views import list_books, LibraryDetailView
# from .views import RegisterView, CustomLoginView, CustomLogoutView
# from .views import admin_view, librarian_view, member_view
# urlpatterns = [
#     path('books/', list_books, name='list_books'),
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', CustomLogoutView.as_view(), name='logout'),
#     path('register/', views.register, name='register'),
#     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
#     path('admin-area/', admin_view.admin_view, name='admin_view'),
#     path('librarian-area/', librarian_view.librarian_view, name='librarian_view'),
#     path('member-area/', member_view.member_view, name='member_view'),
#     path('librarian/', LibrarianView.as_view(), name='librarian_view'),
#     path('member/', member_view, name='member_view'),
#     path('admin/', admin_view, name='admin_view'),
#     path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),
#     path('books/add/', views.add_book, name='add_book'),
#     path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),

# ]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    LibrarianView, list_books, LibraryDetailView,
    RegisterView, CustomLoginView, CustomLogoutView,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)

urlpatterns = [
    # Authentication views
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Optionally also support default Django auth views
    path('login-alt/', LoginView.as_view(template_name='relationship_app/login.html'), name='login_alt'),
    path('logout-alt/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_alt'),

    # Book listing and library detail
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin-area/', admin_view, name='admin_view'),
    path('librarian-area/', librarian_view, name='librarian_view'),
    path('member-area/', member_view, name='member_view'),

    # Alternative class-based view for librarian if needed
    path('librarian/', LibrarianView.as_view(), name='librarian_cbv'),

    # Book management views
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', delete_book, name='delete_book'),
]
