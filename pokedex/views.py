from django.shortcuts import render

# Create your views here.
def index(request):
    pokemon = [ "pikachu", "charmander", "bulbasaur", "squirtle"] 
    return render(request, 'index.html')