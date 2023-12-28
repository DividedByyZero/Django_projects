from django.shortcuts import render
from django.http import HttpResponse
from Library.models import *
from Library import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/Library')
            else:
                return HttpResponse("Please Login!")
        else:
            return HttpResponse("Login Details are not correct!")
    else : 
        return render(request,'Library/login.html',context={})

@login_required   
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('registration'))

def registration(request):
    register = False
    dict={}
    if request.method == 'POST':
        mainform = forms.UserFormmain(data = request.POST)
        notmainform = forms.userFormnot(data = request.POST)
        if mainform.is_valid() and notmainform.is_valid():
            user = mainform.save()
            user.set_password(user.password)
            user.save()
            user_info = notmainform.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES : 
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            register = True
    main_user = forms.UserFormmain
    u_user = forms.userFormnot
    dict = {'main_Form' : main_user , 'not_user' : u_user ,'is_registered' : register}
    return render(request,'Library/home.html',context=dict)

def home(request):
    # current_user = request.user
    # print(current_user.username)
    # print(current_user.password)
    dict={}
    return render(request,'Library/index.html',context=dict)

def StudentReg(request):
    student_form = forms.StudentRegistration()
    dict={'Student' : student_form}
    if request.method == 'POST':
        student_form = forms.StudentRegistration(request.POST)
        if student_form.is_valid():
            student_form.save(commit=True)
            return redirect('/Library')
    return render(request,'Library/StudentRegForm.html',context=dict)

def addBook(request):
    book_form = forms.BookForm()
    dict={'Book' : book_form}
    if request.method == 'POST':
        book_form = forms.BookForm(request.POST)
        if book_form.is_valid():
            book_form.save(commit=True)
            return redirect('/Library')
    return render(request,'Library/Book.html',context=dict)
def borrow(request):
    track_form = forms.TrackForm()
    dict={'Track' : track_form}
    if request.method == 'POST':
        track_form = forms.TrackForm(request.POST)
        if track_form.is_valid():
            track_form.save(commit=True)
            return redirect('/Library')
    return render(request,'Library/track.html',context=dict)

def booklist(request):
    All_books = Books.objects.order_by('Book_title')
    dict={'books':All_books}
    return render(request,'Library/book_list.html',context=dict)
def editBook(request,id):
    book_info = Books.objects.get(Book_id=id)
    edit_form = forms.BookForm(instance=book_info)
    dict={'x':edit_form,'id':book_info.Book_id}
    if request.method == 'POST':
        edit_form = forms.BookForm(request.POST,instance=book_info)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return redirect('/Library')
        else:
            print("Not Valid")
    return render(request,'Library/edit.html',context=dict)
def deleteBook(request,idx):
    book_info = Books.objects.get(Book_id=idx).delete()
    return render(request,'Library/delete.html',context={})