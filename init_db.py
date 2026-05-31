import sqlite3
from config import Config

def init_database():
    """Inizializza il database SQLite con la tabella ANIME_MANGA"""
    conn = sqlite3.connect(Config.DATABASE)
    cursor = conn.cursor()
    
    # Crea la tabella
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS anime_manga (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            genere TEXT,
            anno INTEGER,
            trama TEXT,
            rating REAL,
            immagine_url TEXT,
            num_stagioni INTEGER DEFAULT 1,
            episodi_per_stagione TEXT,
            num_capitoli INTEGER,
            pagine_per_capitolo TEXT,
            data_aggiunta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database inizializzato correttamente!")

if __name__ == '__main__':
    init_database()
