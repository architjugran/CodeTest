from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, NoteForm
from django.template import loader
from django.http import HttpResponse
from .models import Note

# Create your views here.
def logoutUser(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
    return render(request, 'registerForm.html')

def home(request):
    if request.user.is_authenticated: # if user is logged in, filter his notes and show them on the page
        notes = Note.objects.filter(user=request.user)
        context = {'notes': notes}
        return render(request, 'note.html', context)
    return redirect('/login_user/') # if user is not logged in, display login page

def createNote(request):
    if not request.user.is_authenticated:# if user is not logged in, display login page
        return redirect('/login_user/') 
    else:#else open the form page, then when user enters data, save the data into the database and redirect to home page to show the new list of notes
        form = NoteForm(request.POST or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('/')
        context = {
            "form": form,
        }
        return render(request, 'noteForm.html', context)

def editNote(request,pk):#when edit button is clicked, first control goes into else block and user is shown form page, then on clicking Submit- control will go to if block
    info = Note.objects.get(id=pk)
    if request.method == "POST":
        form = NoteForm(request.POST or None, instance=info)
        if form.is_valid():
            eduinfo = form.save(commit=False)#saving new information
            eduinfo.user = request.user
            eduinfo.save()
            return redirect('/')
    else:
        form = NoteForm(instance=info)
    return render(request, 'noteForm.html', {'form': form})

def deleteNote(request,pk):
    instance = Note.objects.get(id=pk)#get note object from database with corresponding id
    instance.delete()#delete note object
    return redirect('/')