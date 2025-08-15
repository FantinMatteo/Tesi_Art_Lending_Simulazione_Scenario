# Dataset: Aste di Felice Casorati (2005-2023)

### Descrizione

Questo dataset raccoglie i dati delle vendite registrate all'asta dall'artista Felice Casorati nell'intervallo temporale 2005-2023.
L'insieme dei dati raccolti è stato utilizzato nel contesto della tesi "Art Lending - Impiego di strumenti innovativi nell’ambito della 
valorizzazione culturale"
per sottolineare le caratteristiche chiave del mercato di riferimento e costruire la simulazione finanziaria dell'operazione.

### Struttura e Contenuto

Il dataset è composto da due file:

*database_casorati.xlsx: Il file in formato Excel con i dati grezzi.

*database_casorati_pulito.csv: Una versione del dataset pulita e pronta per l'analisi, salvata in formato CSV per garantire la massima 
compatibilità con gli strumenti di analisi dati (es. Python, R).

### Anteprima del Dataset Pulito

                                    Opera  Genere  Data Asta  Estimate_min  Estimate_Max  Hammer_p
0    Le Pere Verdi o Quattro Pere sul Pan       0 2023-11-28         20000         30000     46800
1                  Figura con Ma sul Viso       1 2021-11-18          2000          3000      2750
2                                    Nudo       1 2020-12-12          4500          6000      3800
3                                    Nudo       1 2020-12-12          4500          6000      3800
4                     Nudi nello Studio**       1 2020-12-12         10000         15000     11000

### Fonte dei Dati

I dati sono stati raccolti manualmente da banche dati di case d'asta e database di mercato.

### Note 

Nel dataset, gli asterischi accanto al nome dell'opera indicano il numero di volte che l'opera è stata battuta all'asta, come segue:
Nessun asterisco: l'opera è stata venduta per la prima volta.
Un asterisco (*): l'opera è stata venduta per la seconda volta.
Due asterischi (**): l'opera è stata venduta per la terza volta.

Nel dataset pulito la colonna (Genere) specifica la natura dell'opera:
(1) indica che si tratta di un dipinto
(0) indica che si tratta di altro
