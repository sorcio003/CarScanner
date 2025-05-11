# 🚗 CarScanner – Il tuo radar per concessionarie auto! 🔍

**CarScanner** è un bot in Python progettato per semplificarti la vita: trova automaticamente tutte le **concessionarie di auto** in una città a tua scelta sfruttando la potenza di **Google Maps**. Nessuna ricerca manuale, nessun clic inutile. Tu scegli la città, lui fa il resto.

---

## ⚙️ Cosa fa CarScanner?

- 🔎 **Ricerca Intelligente**  
  Trova tutte le concessionarie semplicemente specificando una città: ad esempio “Concessionaria Auto, Milano”.

- 🍪 **Gestione Automatica dei Cookie**  
  Addio fastidiosi popup! CarScanner li accetta automaticamente.

- 🎯 **Dati Precisi e Utili**  
  Estrae e restituisce il nome di ogni concessionaria direttamente da Google Maps.

- 🧠 **Semplice e Intuitivo**  
  Ti basta cambiare UNA riga per cercare nella tua città preferita. Nessuna configurazione complicata.

---

## 🚀 Come iniziare in 3 minuti

### 1. Clona il repository

```bash
git clone https://github.com/tuo-username/carscanner.git
cd carscanner
```

### 2. Installa le dipendenze

CarScanner utilizza **Selenium** e **webdriver-manager** per interagire con il browser:

```bash
pip install -r requirements.txt
```

*(oppure direttamente con:)*  
```bash
pip install selenium webdriver-manager
```

### 3. Lancia il bot!

Apri il file Python, imposta la tua città preferita nella variabile di ricerca e avvia lo script:

```python
city = "Concessionaria Auto, Roma"
```

E poi esegui:

```bash
python carscanner.py
```

---

## 💡 Esempi d’Uso

- Pianifichi di cambiare auto? Ottieni subito una lista di concessionarie nella tua zona.
- Sei uno sviluppatore o un marketer? Puoi integrare i risultati in altri progetti.
- Vuoi fare scraping locale per analisi di mercato? CarScanner è perfetto per iniziare.

---

## 🛠️ Requisiti

- Python 3.7+
- Google Chrome installato
- WebDriver compatibile (gestito automaticamente da `webdriver-manager`)

---

## 📌 Note aggiuntive

- Ricorda che l’uso eccessivo di scraping su Google Maps può violare i loro termini di servizio. Usalo con buon senso e per scopi leciti.
- Per miglioramenti futuri, è possibile estendere il bot per salvare i risultati in CSV, integrarlo con Google Sheets o aggiungere supporto a più tipi di attività commerciali!

---

## 🙌 Contribuisci o lascia una ⭐

Ti piace il progetto? Lascia una ⭐ o proponi una feature! Ogni contributo è benvenuto.
