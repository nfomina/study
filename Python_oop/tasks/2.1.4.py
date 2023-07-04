import sys
from collections import Counter


pokemons = Counter([pokemon.strip() for pokemon in sys.stdin])

print(pokemons.total()-len(pokemons))
