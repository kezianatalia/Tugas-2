from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import change_status
from todolist.views import delete
from todolist.views import show_json
from todolist.views import add_todo

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('change_status/<int:pk>', change_status, name='change_status'),
    path('delete/<int:pk>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todo, name='add_todolist'),
]