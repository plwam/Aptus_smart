from django.shortcuts import render
from library.models import Book
from users.models import Users
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def start(request):

    user=request.user
    
   
    return render(request, "start.html",{'user':user})

def biblio_end(request):

    return render(request, "BIBLO_END.html")

def fav(request):

    return render(request, "fav.html")

def bd(request):

    return render(request, "bd.html")

def histo(request):

    return render(request, "histo.html")

def litterature(request):

    return render(request, "litterature.html")

def programmation(request):
    infos= Book.objects.all()
    return render(request, "anex_prog.html",{'infos': infos})

def items(request):
    
    return render(request,"try_1.html")

