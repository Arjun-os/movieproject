from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Movie
from .forms import Movieform

# Create your views here.


def home(request):
    k = Movie.objects.all()
    return render(request, "home.html", {'m': k})

def addmovie(request):
    if (request.method == "POST"):
        t = request.POST['t']
        d = request.POST['d']
        y = request.POST['y']
        i = request.FILES['i']
        m = Movie.objects.create(title=t, desc=d, year=y , image=i)
        m.save()
        return home(request)
    return render(request, "addmovie.html" )

def moviedetails(request, p):
    d = Movie.objects.get(id=p)
    return render(request, "moviedetails.html", {'d': d})


def movieedit(request, p):
    movie = get_object_or_404(Movie, id=p)

    if request.method == "POST":
        form = Movieform(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return render(request, "moviedetails.html", {'d': movie})
    else:
        form = Movieform(instance=movie)

    return render(request, "editmovie.html", {"form": form})


def deletemovie(request, p):
    movie = Movie.objects.get(id=p)
    movie.delete()
    return render(request,template_name="home.html") # Redirect to the home page or any other desired page
