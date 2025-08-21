import pandas as pd
import numpy as np

# Funzione per trovare tutte le combinazioni di subset
def subset_sum(numbers, target, partial=[], all_combinations=[]):
   
    s = sum(partial)

    # Se la somma è uguale al target è stata trovata una soluzione
    if s == target:
        all_combinations.append(partial)
    
    # Se la somma è maggiore del target = interrompere
    if s >= target:
        return

    # Iteriamo sui numeri rimanenti
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])
    
    return all_combinations

# -- SUBSET SUM PROBLEM --
opere = pd.read_excel('Database_pulito.xlsx')

# L'insieme S è rappresentato dai H_p
prezzi = opere['Hammer_p'].dropna().tolist()
prezzi = [int(p) for p in prezzi if p > 0]

# Il termine T è il valore che deve assumere la garanzia
valore_garanzia = 245000

print(f"Ricerca di combinazioni per un valore di garanzia di {valore_garanzia}€...")

# Eseguire algoritmo
combinazioni_trovate = subset_sum(prezzi, valore_garanzia)

if combinazioni_trovate:
    print(f"\nTrovate {len(combinazioni_trovate)} combinazioni di opere per un valore di {valore_garanzia}€:")
    for i, combo in enumerate(combinazioni_trovate):
        print(f"Combinazione {i+1}: {combo}")
else:
    print("\nNessuna combinazione esatta trovata.")
