# Catalogo Anime & Manga

Sito web di esempio per un progetto scolastico: catalogo di Anime e Manga.

## Descrizione
Applicazione web semplice realizzata con Python + Flask e SQLite. Permette di visualizzare, inserire, cercare, modificare ed eliminare elementi (anime/manga).

## Tecnologie
- Python 3.11+
- Flask
- SQLite
- HTML/CSS (templates Jinja2)
- Vercel (deploy)

## Struttura del repository
- `app.py` — applicazione Flask
- `init_db.py` — script per creare la tabella
- `migrate_db.py` — aggiunge campi al database
- `add_samples.py` — inserisce dati di esempio
- `database.db` — database (ignorato da git)
- `templates/` — file HTML
- `static/` — CSS e JS
- `vercel.json` — configurazione per Vercel

## Istruzioni di esecuzione (locale)
1. Crea un virtualenv e attivalo

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Installa dipendenze

```bash
pip install -r requirements.txt
```

3. Inizializza il database (crea `database.db`)

```bash
python init_db.py
```

4. (Opzionale) Aggiungi dati di esempio

```bash
python add_samples.py
```

5. Avvia l'app

```bash
python app.py
# poi apri http://127.0.0.1:5000
```

## Preparazione e deploy su Vercel
1. Assicurati di avere un repository GitHub per il progetto.
2. Collega il repository a Vercel tramite la dashboard di Vercel.
3. Vercel utilizzerà il file `vercel.json` per eseguire l'app con il builder `@vercel/python`.

## Link pubblici
- Repository GitHub: https://github.com/sertorio2223/anime-manga-catalog
- Sito pubblicato su Vercel: (in aggiornamento...)

