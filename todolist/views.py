from http.client import HTTPResponse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

# TODO: Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.all().order_by('date').values()
    context = {
        'list_todo' : data_todolist,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        date_format = date.strftime("%d %b, %Y, %X")
        finished = False
        Task.objects.create(date=date_format, title=title, description=description,finished=finished, user=request.user)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "add_task.html")

def change_status(request, pk):
    task = Task.objects.get(id=pk)
    task.finished = not(task.finished)
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HTTPResponse(serializers.serialize('json', data_todolist), content_type='application/json')

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        date_format = date.strftime("%d %b, %Y, %X")
        finished = False
        todo = Task.objects.create(date=date_format, title=title, description=description,finished=finished, user=request.user)
        return JsonResponse({'pk':todo.pk,
                'fields':{
                'title':todo.title,
                'date':todo.date,
                'description':todo.description,
            }})