from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.forms import ModelForm
from books.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre','pages']

def get_book(book_id):
  return Book.objects.get(id=book_id)

def book_list(request):
    books = Book.objects.all()
    data = {'all_books': books}
    return render(request, 'books/book_list.html', data)

def book_detail(request, book_id):
    book = get_book(book_id)
    data = {'book': book}
    print(request)
    return render(request, 'books/book_detail.html', data)

def book_create(request):
    book_form = BookForm(request.POST or None)
    if book_form.is_valid():
        book_form.save()
        return redirect('books:book_list')
    data = {'form': book_form, 'new_or_edit': 'New'}
    return render(request, 'books/book_form.html', data)

def book_update(request, book_id):
    book = get_book(book_id)
    book_form = BookForm(request.POST or None, instance=book)
    if book_form.is_valid():
        book_form.save()
        return redirect('books:book_list')
    data = {'form': book_form, 'new_or_edit': 'Edit'}
    return render(request, 'books/book_form.html', data)

def book_remove(request, book_id):
    book = get_book(book_id)
    if request.method=='POST':
        book.delete()
        return redirect('books:book_list')
    data = {'book':book}
    return render(request, 'books/book_confirm_delete.html', data)