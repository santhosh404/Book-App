from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from . models import *




def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if(User.objects.filter(email = email).exists()):
                return render(request, 'signup.html', {'email_error':'Email already exists!'})
            else:
                user = User.objects.create_user(email=email, username=username,  password=password)
                user.save()
                return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'signup.html', {"pass_error":"Passwords doesn't match!"})
    else:
        return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            Login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'login.html', {'error':'Invalid credentials'})
    return render(request, 'login.html')

        
    
def home(request):
    record = Books.objects.filter(email=request.user.email)
    if(len(record))>0:
        return render(request, 'home.html', {'record':record})
    else:
        return render(request, 'home.html', {'empty':'No Records Found!'})

    return render(request, 'home.html')


def add_books(request):
    if request.method == 'POST':
        email = request.POST['email']
        book = request.POST['book']
        description = request.POST['description']
        if (request.user.email == email):  
            book_form = Books.objects.create(email=email, Book=book, Description=description)
            book_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'addbooks.html', {'email_error':'Invalid Email Id!'})
            
    return render(request, 'addbooks.html')

def update_event(request, update_id):
    update = Books.objects.filter(id=update_id)
    if request.method == 'POST':
        book = request.POST(['book'], instance=update)
        description = request.POST(['description'], instance=update)
        if (request.user.email == email):  
            Book
            book_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'update.html', {'email_error':'Invalid Email Id!'})
    return render(request, 'update.html')

def delete_event(request, book_id):
    delete_post = Books.objects.filter(id=book_id)
    print(delete_post)
    delete_post.delete()
    return HttpResponseRedirect(reverse('home'))


def logout(request):
    Logout(request)
    return HttpResponseRedirect(reverse('login'))

    