from django.shortcuts import render

# Create your views here.
def show_mywatchlist(request):
    return render(request, "mywatchlist.html")

from django.shortcuts import render
from mywatchlist.models import MyWatchList

# TODO: Create your views here.
def show_mywatchlist(request):
    movies_data = MyWatchList.objects.all()
    context = {
        'list_movies' : movies_data,
        'nama' : 'Kezia Natalia',
        'student_id' : '2106703891'
    }
    return render(request, "mywatchlist.html", context)


