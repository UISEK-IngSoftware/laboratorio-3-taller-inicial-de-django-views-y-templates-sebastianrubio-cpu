from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = [ "pikachu", "charmander", "bulbasaur", "squirtle", "pidgey", "rattata", "zubat", "geodude", "onix", "psyduck" , "meowth", "jigglypuff", "gengar", "eevee", "snorlax", "mewtwo", "mew", "articuno", "zapdos", "moltres", "dragonite" ] 
    return render(request, 'index.html', {'pokemons': pokemons})


def pokemon_details(request, pokemon):
    return render(request, 'details.html', {'pokemon': pokemon})