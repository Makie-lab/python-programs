import array
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("--------------------------------")
print("|         Pokedex Sorter.      |")
print("--------------------------------")
print("a. Evolution Stage")
print("b. Generation")
print("c. Health")
print("d. Types")
print("e. Names")

choice = input("Choose an option to sort by (a-e): ")

if choice == 'a':
    print("Sorting by Evolution Stage...")
if choice == 'b':
    print("Sorting by Generation...")
if choice == 'c':       
    print("Sorting by Health...")
if choice == 'd':
    print("Sorting by Types...")
if choice == 'e':
    print("Sorting by Names...")
else :
    print("Invalid choice. Please select a valid option (a-e).")
    exit()

print("Sorting started at:", now)
print("-" * 40)

def pokedex_sort(pokedex):
    n = len(pokedex)

    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if pokedex[j] < pokedex[min_index]:
                min_index = j
                
        pokedex[i], pokedex[min_index] = pokedex[min_index], pokedex[i]
        
    return sorted(pokedex)

    evol_stage = 1 #evolstageascending
    generation = 2 #generationascending
    health = 3 #healthlow to high
    types = 4 #types
    names= 5 #names alphabetical
    
    pokedex = [
    {"name": "Frogradier", "evol_stage": 2, "generation": 6, "health": 54, "type": "Water"},
    {"name": "Blaziken", "evol_stage": 3, "generation": 3, "health": 80, "type": "Fire/Fighting"},
    {"name": "Eevee", "evol_stage": 1, "generation": 1, "health": 55, "type": "Normal"},
    {"name": "Sylveon", "evol_stage": 2, "generation": 6, "health": 95, "type": "Fairy"},
    {"name": "Dark Tyranitar", "evol_stage": 3, "generation": 2, "health": 100, "type": "Rock/Dark"},
    {"name": "Abra", "evol_stage": 1, "generation": 1, "health": 25, "type": "Psychic"}
]
    
    sorted_pokemons = pokedex_sort(pokedex)
    