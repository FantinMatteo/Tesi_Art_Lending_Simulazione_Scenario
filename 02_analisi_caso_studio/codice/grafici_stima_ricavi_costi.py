import pandas as pd
import matplotlib.pyplot as plt

# Salvare stima costi in formato csv 
costi = pd.read_excel('stima_costi.xlsx')
costi.to_csv("stima_costi.csv", index=False)
print ("costi salvati in csv")
# Salvare stima ricavi in formato csv 
ricavi = pd.read_excel("stima_ricavi.xlsx")
ricavi.to_csv("stima_ricavi.csv", index=False)
print ("ricavi salvati in csv")

# PARTE 1: --GRAFICI COSTI E RICAVI--

# GRAFICO COSTI STIMATI
costi = pd.read_excel('stima_costi.xlsx')
# Estrarre i valori per il grafico a torta
# Valori identifica i costi medi stimati
valori = costi['media']
# Etichette identifica le categorie di spesa
etichette = costi['categoria']
# Grafico a torta
fig, ax = plt.subplots(figsize=(14, 10))
ax.pie(valori, labels=etichette, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 20})
ax.set_title('Percentuale categorie di costo')
# Impostazioni del grafico
plt.title('Costi stimati', fontsize=24, color='darkred', fontweight='bold')
# Salvare il grafico
plt.savefig('percentuale_costi.png')
print("1) Grafico costi generato")

# GRAFICO RICAVI STIMATI
ricavi = pd.read_excel("stima_ricavi.xlsx")
# Estrarre i valori per il grafico a torta
# Valori identifica i ricavi medi stimati
valori = ricavi["media"]
# Etichette identifica le categorie di ricavo
etichette = ricavi["Categoria"]
# Grafico a torta
fig, ax = plt.subplots(figsize=(14, 10))
ax.pie(valori, labels=etichette, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 20})
ax.set_title('Percentuale categorie di ricavo')
# Impostazioni del grafico
plt.title('Ricavi stimati', fontsize=24, color='darkred', fontweight='bold')
# Salvare il grafico
plt.savefig('percentuale_ricavi.png')
print("2) Grafico ricavi generato")

#PARTE 2: --SIMULAZIONI MONTE CARLO--
import numpy as np

# Simulazione dei Costi
# Estrarre i valori per la simulazione
dettaglio_costi=pd.read_excel("dettaglio_costi.xlsx")
dc = dettaglio_costi 

# Dati per la simulazione
numero_simulazioni = 10000
costi_totali_simulati = []

# Eseguire la simulazione Monte Carlo
for _ in range(numero_simulazioni):
    costo_totale = 0
    # Per ogni categoria, genera un costo casuale nell'intervallo specificato
    for index, row in dc.iterrows():
        costo_casuale = np.random.uniform(row['p_min'], row['p_Max'])
        costo_totale += costo_casuale
    costi_totali_simulati.append(costo_totale)
    # Converti i risultati in un DataFrame per l'analisi
df_risultati = pd.DataFrame(costi_totali_simulati, columns=['Costo Totale (€)'])

# Calcola le statistiche chiave
media = df_risultati['Costo Totale (€)'].mean()
mediana = df_risultati['Costo Totale (€)'].median()
primo_quartile = df_risultati['Costo Totale (€)'].quantile(0.25)
terzo_quartile = df_risultati['Costo Totale (€)'].quantile(0.75)

# Creazione grafico 
fig, ax = plt.subplots(figsize=(10, 6))
df_risultati.hist(ax=ax, bins=50, color='red', edgecolor='black', alpha=0.7)

# Linee verticali
ax.axvline(media, color='black', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}€')
ax.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana:.2f}€')
ax.axvline(primo_quartile, color='blue', linestyle='dashed', linewidth=2, label=f'Q1: {primo_quartile:.2f}€')
ax.axvline(terzo_quartile, color='orange', linestyle='dashed', linewidth=2, label=f'Q3: {terzo_quartile:.2f}€')

# Impostazioni del grafico
ax.set_title('Distribuzione dei Costi Totali (Simulazione Monte Carlo)')
ax.set_xlabel('Costo Totale (€)')
ax.set_ylabel('Frequenza')
ax.legend()

# Salvare il grafico
plt.tight_layout()
plt.savefig('distribuzione_costi.png')

print("Simulazione Monte Carlo costi completata")
print(f"Costo medio: {media:.2f} €")
print(f"Mediana: {mediana:.2f} €")
print(f"Primo quartile: {primo_quartile:.2f} €")
print(f"Terzo quartile: {terzo_quartile:.2f} €")
print("3) Grafico generato e salvato come distribuzione_costi.png")

# Simulazione dei ricavi
# Estrarre i valori per la simulazione
ricavi = pd.read_excel("stima_ricavi.xlsx")

# Dati per la simulazione
numero_simulazioni = 10000
ricavi_totali_simulati = []

# Eseguire la simulazione Monte Carlo
for _ in range(numero_simulazioni):
    ricavo_totale = 0
    # Per ogni categoria, genera un costo casuale nell'intervallo specificato
    for index, row in ricavi.iterrows():
        ricavo_casuale = np.random.uniform(row['min'], row['max'])
        ricavo_totale += ricavo_casuale
    ricavi_totali_simulati.append(ricavo_totale)
    # Converti i risultati in un DataFrame per l'analisi
df_risultati = pd.DataFrame(ricavi_totali_simulati, columns=['Ricavo Totale (€)'])

# Calcola le statistiche chiave
media = df_risultati['Ricavo Totale (€)'].mean()
mediana = df_risultati['Ricavo Totale (€)'].median()
primo_quartile = df_risultati['Ricavo Totale (€)'].quantile(0.25)
terzo_quartile = df_risultati['Ricavo Totale (€)'].quantile(0.75)

# Creazione grafico 
fig, ax = plt.subplots(figsize=(10, 6))
df_risultati.hist(ax=ax, bins=50, color='green', edgecolor='black', alpha=0.7)

# Linee verticali
ax.axvline(media, color='black', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}€')
ax.axvline(mediana, color='red', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana:.2f}€')
ax.axvline(primo_quartile, color='blue', linestyle='dashed', linewidth=2, label=f'Q1: {primo_quartile:.2f}€')
ax.axvline(terzo_quartile, color='orange', linestyle='dashed', linewidth=2, label=f'Q3: {terzo_quartile:.2f}€')

# Impostazioni del grafico
ax.set_title('Distribuzione dei Ricavi Totali (Simulazione Monte Carlo)')
ax.set_xlabel('Ricavo Totale (€)')
ax.set_ylabel('Frequenza')
ax.legend()

# Salvare il grafico
plt.tight_layout()
plt.savefig('distribuzione_ricavi.png')

print("Simulazione Monte Carlo ricavi completata")
print(f"Ricavo medio: {media:.2f} €")
print(f"Mediana: {mediana:.2f} €")
print(f"Primo quartile: {primo_quartile:.2f} €")
print(f"Terzo quartile: {terzo_quartile:.2f} €")
print("4) Grafico generato e salvato come distribuzione_ricavi.png")

# Simulazione del margine medio
# Estrarre i valori per la simulazione
costi = pd.read_excel("dettaglio_costi.xlsx")
ricavi = pd.read_excel("stima_ricavi.xlsx")

# Dati per la simulazione
numero_simulazioni = 10000
margini_simulati = []

# Esegui la simulazione Monte Carlo
for _ in range(numero_simulazioni):
    costo_totale = 0
    ricavo_totale = 0
    # Genera un costo casuale per ogni categoria
    for index, row in costi.iterrows():
        costo_casuale = np.random.uniform(row['p_min'], row['p_Max'])
        costo_totale += costo_casuale
    # Genera un ricavo casuale per ogni categoria
    for index, row in ricavi.iterrows():
        ricavo_casuale = np.random.uniform(row['min'], row['max'])
        ricavo_totale += ricavo_casuale
    
    # Calcola il margine e aggiungilo alla lista
    margine = ricavo_totale - costo_totale
    margini_simulati.append(margine)

# Convertire i risultati in un DataFrame per l'analisi
df_risultati_margine = pd.DataFrame(margini_simulati, columns=['Margine Totale (€)'])

# Creare il grafico
fig, ax = plt.subplots(figsize=(10, 6))
df_risultati_margine.hist(ax=ax, bins=50, color='black', edgecolor='black', alpha=0.7)
plt.xlim(left=min(df_risultati_margine['Margine Totale (€)']), right=0)

# Impostazioni del grafico
ax.set_title('Distribuzione del Margine Totale (Simulazione Monte Carlo)')
ax.set_xlabel('Margine Totale (€)')
ax.set_ylabel('Frequenza')

plt.tight_layout()
plt.savefig('distribuzione_margine.png')

print("Simulazione Monte Carlo margine completata")
print(f"Margine medio: {media:.2f} €")
print(f"Mediana: {mediana:.2f} €")
print(f"Primo quartile: {primo_quartile:.2f} €")
print(f"Terzo quartile: {terzo_quartile:.2f} €")
print("5) Grafico generato e salvato come distribuzione_margine.png")
