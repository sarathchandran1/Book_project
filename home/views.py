from django.shortcuts import render,redirect
from .forms import Autherform,Bookform
from django.db.models import Q
from . models import Book
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage

# Create your views here.


def createBook(request):
    books = Book.objects.all()
    
    if request.method=='POST':

        form=Bookform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')

           

    else:
        form = Bookform()

    return render(request,'book.html',{'form':form,'books':books})


def Create_Auther(request):
    if request.method=='POST':
        form = Autherform(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
        
    else:
        form=Autherform()
    return render(request,'auther.html',{'form':form})





def list_book(request):
    book = Book.objects.all()
    paginator = Paginator(book,2)
    page_number = request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    
    except EmptyPage:
        page=paginator.page(page_number.num_pages)


    return render(request,'listbook.html',{'books':book,'page':page})


def deatiles_View(request,book_id):

    book = Book.objects.get(id=book_id)
    return render(request,'list.html',{'books':book})

def updateBook(request,book_id):

    book = Book.objects.get(id=book_id)
    if request.method=='POST':
        form = Bookform(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Bookform(instance=book)
    return render(request,'update.html',{'form':form})
            


    


def deleteView(request,book_id):
    book = Book.objects.get(id = book_id)
    if request.method=='POST':
        book.delete()

        return redirect('/')

    

    return render(request,'delete.html',{'books':book})



def index(request):
    return render(request,'base.html')


def search_book(request):
    query = None
    books = None

    if 'q' in request.GET:

        query=request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query))

    else:
        books=[]
    
    context={'books':books,'query':query}

    return render(request,'search.html',context)

















