from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)



def add_book(request):
    Book.objects.create(title=request.POST["title"], desc=request.POST["description"])
    return redirect("/")



def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)



def add_author(request):
    Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"])
    return redirect("/authors")



def view_book(request, book_id):
    context= {
        "book": Book.objects.get(id = book_id),
        "authors": Author.objects.all(),
    }
    return render(request, 'viewBook.html', context)



def add_author_to_book(request, book_id):
    this_book = Book.objects.get(id = book_id)
    this_author = Author.objects.get(id = request.POST["author_id"])
    this_book.authors.add(this_author)
    # return redirect('/books/ + str(this_book.id)')
    return redirect("/book/"+str(this_book.id))



def view_author(request, author_id):
    context= {
        "author": Author.objects.get(id = author_id),
        "books": Book.objects.all(),
    }
    return render(request, "viewAuthor.html", context)




def add_book_to_author(request, author_id):
    this_author = Author.objects.get(id = author_id)
    this_book = Book.objects.get(id = request.POST["book_id"])
    this_author.books.add(this_book)
    return redirect("/authors/"+str(this_author.id))

