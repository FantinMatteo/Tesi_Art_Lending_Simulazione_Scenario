import pandas as pd
import matplotlib.pyplot as plt

#PARTE1: ---PREPARAZIONE DATI---

#Leggiamo il dataset delle vendite all'asta di Casorati, in versione pulita = 220 osservazioni
df_Casorati = pd.read_excel('Database_pulito.xlsx')
#Salvare dataset in formato csv 
df_Casorati.to_csv('database_casorati_pulito.csv', index=False)
#Semplificare nomenclatura dataframe
dfc = df_Casorati
#trasformare i dati della colonna "Data Asta" in formato Data
dfc['Data Asta'] = pd.to_datetime(dfc['Data Asta'])

#PARTE 2: ---GRAFICI DATASET---

#Grafico andamento dei prezzi registrati all'asta da Casorati tra il 2005 e il 2023
dfc_andamento = dfc.groupby(dfc['Data Asta'].dt.year)['Hammer_p'].mean().reset_index()
dfc_andamento.columns = ['Anno', 'Prezzo Medio (€)']
#Personalizzare il grafico
plt.figure(figsize=(10, 6))
plt.plot(dfc_andamento['Anno'], dfc_andamento['Prezzo Medio (€)'], marker='o', linestyle='-', color='r')
plt.title('Andamento dei prezzi delle opere di Felice Casorati (2005-2023)')
plt.xlabel('Anno')
plt.ylabel('Prezzo Medio (€)')
plt.grid(True)
plt.xticks(dfc_andamento['Anno'], rotation=45)
plt.tight_layout()
#Salvare grafico
plt.savefig('prezzo_medio_casorati.png')
print("1) grafico andamento prezzi generato")

#Grafico numero di aste di Felice Casorati ogni anno tra il 2005 e il 2023
dfc_aste = dfc.groupby(dfc['Data Asta'].dt.year).size().reset_index(name='Numero di aste')
#Creiamo il grafico 
plt.figure(figsize=(12, 7))
plt.bar(dfc_aste['Data Asta'], dfc_aste['Numero di aste'], color='r')
#Personalizzare il grafico
plt.title('Numero di aste per anno di Felice Casorati (2005-2023)')
plt.xlabel('Anno')
plt.ylabel('Numero di aste')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(dfc_aste['Data Asta'], rotation=45)
plt.tight_layout()
# Salvare grafico
plt.savefig('numero_aste_casorati.png')
print("2) grafico numero aste generato")

#Grafico di confronto tra prezzo di stima e prezzo di martello
dfc_confronto = dfc.groupby(dfc['Data Asta'].dt.year)[['Estimate_min', 'Estimate_Max', 'Hammer_p']].mean().reset_index()
#Prezzo di stima medio
dfc_confronto['Prezzo_Stima_Medio'] = (dfc_confronto['Estimate_min'] + dfc_confronto['Estimate_Max']) / 2
#Creiamo il grafico
plt.figure(figsize=(12, 7))
plt.plot(dfc_confronto['Data Asta'], dfc_confronto['Prezzo_Stima_Medio'], marker='o', linestyle='-', color='b', label='Prezzo di Stima Medio')
plt.plot(dfc_confronto['Data Asta'], dfc_confronto['Hammer_p'], marker='o', linestyle='-', color='r', label='Prezzo Martello')
#Personalizzare il grafico
plt.title('Confronto tra prezzo di stima e prezzo di martello (2005-2023)')
plt.xlabel('Anno')
plt.ylabel('Prezzo Medio (€)')
plt.grid(True)
plt.legend()
plt.xticks(dfc_confronto['Data Asta'], rotation=45)
plt.tight_layout()
#Salvare grafico
plt.savefig('confronto_prezzi.png')
print("3) grafico di confronto prezzi generato")

