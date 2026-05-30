import sqlite3
from config import Config

samples = [
    {
        'titolo': 'Fullmetal Alchemist: Brotherhood',
        'tipo': 'Anime',
        'genere': 'Azione, Avventura, Drammatico',
        'anno': 2009,
        "trama": "Due fratelli usano l'alchimia nella speranza di recuperare i loro corpi dopo un esperimento fallito.",
        'rating': 9.1,
        'immagine_url': '',
        'num_stagioni': 1,
        'episodi_per_stagione': 'S1: 64ep'
    },
    {
        'titolo': 'Naruto',
        'tipo': 'Manga',
        'genere': 'Azione, Avventura',
        'anno': 1999,
        'trama': 'La storia di Naruto Uzumaki, un giovane ninja che aspira a diventare Hokage.',
        'rating': 8.0,
        'immagine_url': '',
        'num_stagioni': 5,
        'episodi_per_stagione': 'S1: 220, S2: 500'
    },
    {
        'titolo': 'One Piece',
        'tipo': 'Manga',
        'genere': 'Azione, Avventura, Fantasy',
        'anno': 1997,
        'trama': 'Monkey D. Luffy e la sua ciurma cercano il tesoro leggendario "One Piece".',
        'rating': 8.9,
        'immagine_url': '',
        'num_stagioni': 20,
        'episodi_per_stagione': 'S1: 61, S2: 33, ...'
    },
    {
        'titolo': 'Demon Slayer: Kimetsu no Yaiba',
        'tipo': 'Anime',
        'genere': 'Azione, Fantasy, Drammatico',
        'anno': 2019,
        'trama': "Un ragazzo diventa un cacciatore di demoni per salvare sua sorella e vendicare la sua famiglia.",
        'rating': 8.7,
        'immagine_url': '',
        'num_stagioni': 3,
        'episodi_per_stagione': 'S1: 26, S2: 18, S3: 11'
    }
]

conn = sqlite3.connect(Config.DATABASE)
cur = conn.cursor()
for s in samples:
    cur.execute('''
        INSERT INTO anime_manga (titolo, tipo, genere, anno, trama, rating, immagine_url, num_stagioni, episodi_per_stagione)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (s['titolo'], s['tipo'], s['genere'], s['anno'], s['trama'], s['rating'], s['immagine_url'], s['num_stagioni'], s['episodi_per_stagione']))

conn.commit()
conn.close()
print('✅ Sample data inserita correttamente')
