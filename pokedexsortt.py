from datetime import datetime
import time
import math

start_time = time.perf_counter()

type_order = {
    "Normal": 1, "Fire": 2, "Water": 3, "Electric": 4, 
    "Grass": 5, "Ice": 6, "Fighting": 7, "Poison": 8,
    "Ground": 9, "Flying": 10, "Psychic": 11, "Bug": 12,
    "Rock": 13, "Ghost": 14, "Dragon": 15, "Steel": 16, 
    "Dark": 17, "Fairy": 18
}

dict_strengths = {
    "Normal": [],
    "Fire": ["Grass", "Ice", "Bug", "Steel"],
    "Water": ["Fire", "Ground", "Rock"],
    "Electric": ["Water", "Flying"],
    "Grass": ["Water", "Ground", "Rock"],
    "Ice": ["Grass", "Ground", "Flying", "Dragon"],
    "Fighting": ["Normal", "Ice", "Rock", "Dark", "Steel"],
    "Poison": ["Grass", "Fairy"],
    "Ground": ["Fire", "Electric", "Poison", "Rock", "Steel"],
    "Flying": ["Grass", "Fighting", "Bug"],
    "Psychic": ["Fighting", "Poison"],
    "Bug": ["Grass", "Psychic", "Dark"],
    "Rock": ["Fire", "Ice", "Flying", "Bug"],
    "Ghost": ["Psychic", "Ghost"],
    "Dragon": ["Dragon"],
    "Steel": ["Ice", "Rock", "Fairy"],
    "Dark": ["Psychic", "Ghost"],
    "Fairy": ["Fighting", "Dragon", "Dark"]
}

dict_weakness = {
    "Normal": ["Fighting"],
    "Fire": ["Water", "Ground", "Rock"],
    "Water": ["Electric", "Grass"],
    "Electric": ["Ground"],
    "Grass": ["Fire", "Ice", "Poison", "Flying", "Bug"],
    "Ice": ["Fire", "Fighting", "Rock", "Steel"],
    "Fighting": ["Flying", "Psychic", "Fairy"],
    "Poison": ["Ground", "Psychic"],
    "Ground": ["Water", "Grass", "Ice"],
    "Flying": ["Electric", "Ice", "Rock"],
    "Psychic": ["Bug", "Ghost", "Dark"],
    "Bug": ["Fire", "Flying", "Rock"],
    "Rock": ["Water", "Grass", "Fighting", "Ground", "Steel"],
    "Ghost": ["Ghost", "Dark"],
    "Dragon": ["Ice", "Dragon", "Fairy"],
    "Steel": ["Fire", "Fighting", "Ground"],
    "Dark": ["Fighting", "Bug", "Fairy"],
    "Fairy": ["Poison", "Steel"]
}

pokedex = [
    {"name": "Greninja", "evol_stage": 3, "generation": 6, "health": 130, "type": "Water", "strength": "Fire, Ground, Rock", "weakness": "Electric, Grass"},
    {"name": "Bulbasaur", "evol_stage": 1, "generation": 1, "health": 70, "type": "Grass", "strength": "Water, Ground, Rock", "weakness": "Fire, Ice, Poison, Flying, Bug"},
    {"name": "Lucario", "evol_stage": 2, "generation": 4, "health": 110, "type": "Fighting", "strength": "Normal, Ice, Rock, Dark, Steel", "weakness": "Flying, Psychic, Fairy"},
    {"name": "Pikachu", "evol_stage": 1, "generation": 1, "health": 60, "type": "Electric", "strength": "Water, Flying", "weakness": "Ground"},
    {"name": "Gardevoir EX", "evol_stage": 3, "generation": 3, "health": 310, "type": "Psychic", "strength": "Poison, Ground", "weakness": "Fighting, Poison"},
    {"name": "Charmander", "evol_stage": 1, "generation": 1, "health": 70, "type": "Fire", "strength": "Grass, Ice, Bug, Steel", "weakness": "Water, Ground, Rock"},
    {"name": "Froakie", "evol_stage": 1, "generation": 6, "health": 60, "type": "Water", "strength": "Fire, Ground, Rock", "weakness": "Electric, Grass"},
    {"name": "Ivysaur", "evol_stage": 2, "generation": 1, "health": 110, "type": "Grass", "strength": "Water, Ground, Rock", "weakness": "Fire, Ice, Poison, Flying, Bug"},
    {"name": "Zoroark", "evol_stage": 2, "generation": 5, "health": 100, "type": "Dark", "strength": "Psychic, Ghost", "weakness": "Ice, Dragon, Fairy"},
    {"name": "Charizard", "evol_stage": 3, "generation": 1, "health": 150, "type": "Fire", "strength": "Grass, Ice, Bug, Steel", "weakness": "Water, Ground, Rock"},
    {"name": "Riolu", "evol_stage": 1, "generation": 4, "health": 70, "type": "Fighting", "strength": "Normal, Ice, Rock, Dark, Steel", "weakness": "Flying, Psychic, Fairy"},
    {"name": "Empoleon", "evol_stage": 3, "generation": 4, "health": 140, "type": "Water", "strength": "Fire, Ground, Rock", "weakness": "Electric, Grass"},
    {"name": "Frogradier", "evol_stage": 2, "generation": 6, "health": 80, "type": "Water", "strength": "Fire, Ground, Rock", "weakness": "Electric, Grass"},
    {"name": "Blaziken", "evol_stage": 3, "generation": 3, "health": 100, "type": "Fire", "strength": "Grass, Ice, Bug, Steel", "weakness": "Water, Ground, Rock"},
    {"name": "Eevee", "evol_stage": 1, "generation": 1, "health": 60, "type": "Normal", "strength": "NONE", "weakness": "Fighting"},
    {"name": "Sylveon", "evol_stage": 2, "generation": 6, "health": 90, "type": "Fairy", "strength": "Fighting, Dragon, Dark", "weakness": "Poison, Steel"},
    {"name": "Dark Tyranitar", "evol_stage": 3, "generation": 2, "health": 120, "type": "Dark", "strength": "Psychic, Ghost", "weakness": "Ice, Dragon, Fairy"},
    {"name": "Abra", "evol_stage": 1, "generation": 1, "health": 50, "type": "Psychic", "strength": "Poison, Ground", "weakness": "Fighting, Poison"}
]

total = 0
for i in range(1000000):
    total += i

def pokedex_sort(data_list, key):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            
            if key == 'type':
                val_j = type_order.get(data_list[j][key], 99)
                val_min = type_order.get(data_list[min_index][key], 99)
            else:
                val_j = data_list[j][key]
                val_min = data_list[min_index][key]

            if val_j < val_min:
                min_index = j
                
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    return data_list

running = True
while running:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "="*45)
    print("|            POKEDEX SORTER                 |")
    print("="*45)
    print("a. Evolution Stage")
    print("b. Generation")
    print("c. Health (HP)")
    print("d. Types ")
    print("e. Names")
    print("f. Strength")
    print("g. Weakness")
    print("h. Exit")
    print("-" * 45)

    choice = input("Choose an option (a-h): ").lower().strip()

    sort_map = {
        'a': ('evol_stage', "Evolution Stage"),
        'b': ('generation', "Generation"),
        'c': ('health', "Health"),
        'd': ('type', "Type"),
        'e': ('name', "Name"),
        'f': ('strength', "Strengths"),
        'g': ('weakness', "Weakness"),
        'h': ('exit', "Exit")
    }
    if choice == 'h':
        print("\nExiting Pokedex Sorter (Selection Sort). Thank you!")
        break
    if choice in sort_map:
        key, label = sort_map[choice]
        print(f"\n[Sorting by {label}...]")
        print(f"Time: {now}")
        print("-" * 120)
        
        sorted_list = pokedex_sort(pokedex, key)
        
        print(f"{'NAME':<15} | {'STAGE':<6} | {'GEN':<4} | {'HP':<4} | {'TYPE':<8} | {'STRENGTH':<30} | {'WEAKNESS'}")
        print("-" * 120)
        for p in sorted_list:
            strength = p['strength']
            weakness = p['weakness']
            print(f"{p['name']:15} | {p['evol_stage']:<6} | {p['generation']:<4} | "
            f"{p['health']:<4} | {p['type']:<8} | {strength:<30} | {weakness}")
        print("-" * 120)
        
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        
        print(f"Time Taken: {time_taken:.4f} seconds")
        print("-" * 120)

    else:
        print("\nInvalid choice.")
    
