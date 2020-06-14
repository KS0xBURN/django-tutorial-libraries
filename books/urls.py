from django.urls import path, include
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>', views.book_detail, name='book_view'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:book_id>', views.book_update, name='book_edit'),
    path('delete/<int:book_id>', views.book_remove, name='book_delete'),
]