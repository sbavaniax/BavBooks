# -*- coding: cp1252 -*-
from django.shortcuts import render ,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from Books.models import Book
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def Home(request):
    
    return render(request,"Home.html",{'Books': Book.objects.all()})

def WriteWithUs(request):
    
    return render(request,"WriteWithUs.html")
def MyBook(request,book_id=1):
   
    return render(request,"Book.html",{'MyBok' : Book.objects.get(id=book_id)})

@login_required   
def download(request,download_link='hm.c'):
    
    return HttpResponseRedirect(download_link)

def Categories(request,Categor='Cpp'):
    Books=Book.objects.filter(Category=Categor)
    
    return render(request,"Categories.html",{'Books':Books ,'Cat':Categor})



def Sub_Categories(request,Categor='Cpp'):
    Books_List= Book.objects.filter(Sub_Category=Categor)
    paginator = Paginator(Books_List, 1)
    page = request.GET.get('page')
    try:
        Books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        Books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Books = paginator.page(paginator.num_pages)
    return render(request,"Categories.html",{'Books':Books,'Cat':Categor})




def search_titles(request):
    if request.method=='GET' and 'page' not in request.GET.keys():
        search_text=request.GET['search_text'].strip()
        request.session['search_text']=search_text
    else:
        search_text=request.session['search_text'].strip()

    Bookk=Book.objects.filter(Book_Name__icontains=search_text)
    Book1=Book.objects.filter(ISBN_NBR=search_text)
    Book2=Book.objects.filter(PUB_NAME__icontains=search_text)
    Book3=Book.objects.filter(Author_Name__icontains=search_text)
    Book4=Book.objects.filter(Book_Desc__icontains=search_text)
    red=bool(search_text)
    my_se=[]
    
    if len(Bookk)!= 0 :
        my_se.extend(Bookk)
        
    elif len(Book4)!= 0 :
        my_se.extend(Book4)
        
    if len(Book1)!= 0 :
        my_se.extend(Book1)
        
    if len(Book2)!= 0 :
        my_se.extend(Book2)
        
    if len(Book3)!= 0 :
        my_se.extend(Book3)
    lgth=len(my_se)   
    paginator = Paginator(my_se, 1)
    page = request.GET.get('page')
    try:
        Books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        Books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Books = paginator.page(paginator.num_pages)    
    return  render(request,'search.html',{'nam':Books,'length':lgth,'search':search_text,'red':red})  
