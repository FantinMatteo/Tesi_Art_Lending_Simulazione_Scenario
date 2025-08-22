import pandas as pd
import matplotlib.pyplot as plt

# --GRAFICO DI CONFRONTO TRA PRESTITO CONCESSO E DEBITO ACCUMULATO--
# OPZIONE A
# Dati 
dati = {
    'Categoria': ['Prestito ricevuto', 'Interessi', 'Costo totale'],
    'Valore (€)': [363360, 33465, 396825]
}
grafico = pd.DataFrame(dati)
# Creare il grafico a barre
plt.figure(figsize=(10, 6))
plt.bar(grafico['Categoria'], grafico['Valore (€)'], color=['green', 'red', 'black'])
# Impostazioni grafico
plt.title('Risultati')
plt.ylabel('Valore (€)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Salvare il grafico in un file png
plt.savefig('Opione_A.png')
print("1) Grafico generato e salvato come Opzione_A.png")

# -- GRAFICO CONFRONTO DEBITO RESIDUO OPZIONE A E OPZIONE B --
# Dati 
dati_confronto = {
    'Opzione': ['Opzione A', 'Opzione B'],
    'Debito Residuo (€)': [180465, 160539]
}
debito = pd.DataFrame(dati_confronto)
# Creare grafico a barre
plt.figure(figsize=(8, 6))
plt.bar(debito['Opzione'], debito['Debito Residuo (€)'], color=['lightblue', 'orange'])
# Impostazioni
plt.title('Confronto tra Debito Residuo (Opzione A vs Opzione B)')
plt.xlabel('Opzione di Finanziamento')
plt.ylabel('Debito Residuo (€)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Salvare il grafico in un file png
plt.savefig('confronto_debito_residuo.png')
print("2) Grafico generato e salvato come confronto_debito_residuo.png")
