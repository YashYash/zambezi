from django.shortcuts import render, redirect
from bookselling.forms import BookForm, CustomerForm, GenreForm
from bookselling.models import Book, Customer, Genre


def home(request):
    return render(request, "home.html")


def books(request):
    books = Book.objects.all()
    data = {'books': books}
    return render(request, "books/books.html", {'books': books})


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/books")
    else:
        form = BookForm()
    data = {'form': form}
    return render(request, "books/new_book.html", data)


def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    data = {"book":book}
    return render(request, "books/view_book.html", data)


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            if form.save():
                return redirect("/books/{}".format(book_id))
    else:
        form = BookForm(instance=book)
    data = {"book": book, "form": form}
    return render(request, "books/edit_book.html",data)


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("/books")

def customers(request):
    customers = Customer.objects.all()
    data = {'Customers': customers}
    return render(request, "customers/customers.html", {'Customers': customers})


def new_customer(request):
    if request.method == "POST":
        form2 = CustomerForm(request.POST)
        if form2.is_valid():
            if form2.save():
                return redirect("/customers")
    else:
        form2 = CustomerForm()
    data = {'form2': form2}
    return render(request, "customers/new_customer.html", data)


def view_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    data = {"customer":customer}
    return render(request, "customers/view_customer.html",data)


def edit_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    print customer
    if request.method == "POST":
        form2 = CustomerForm(request.POST, instance=customer)
        print "POST"
        if form2.is_valid():
            if form2.save():
                return redirect("/customers/{}".format(customer_id))
    else:
        form2 = CustomerForm(instance=customer)

    data = {"customer": customer, "form2": form2}
    print form2
    return render(request, "customers/edit_customer.html",data)


def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect("/customers")


def genres(request):
    genres = Genre.objects.all()
    data = {'genres': genres}
    return render(request, "genres/genres.html", {'genres': genres})


def new_genre(request):
    if request.method == "POST":
        form3 = GenreForm(request.POST)
        if form3.is_valid():
            if form3.save():
                return redirect("/genres")
    else:
        form3 = GenreForm()
    data = {'form3': form3}
    return render(request, "genres/new_genre.html", data)


def view_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    data = {"genre": genre}
    return render(request, "genres/view_genre.html",data)


def edit_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    print genre
    if request.method == "POST":
        form3 = GenreForm(request.POST, instance=genre)
        print "POST"
        if form3.is_valid():
            if form3.save():
                return redirect("/genres/{}".format(genre_id))
    else:
        form3 = GenreForm(instance=genre)

    data = {"genre": genre, "form3": form3}
    print form3
    return render(request, "genres/edit_genre.html",data)

def delete_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    genre.delete()
    return redirect("/genres")