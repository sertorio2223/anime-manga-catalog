import sqlite3
from config import Config

def migrate_database():
    """Aggiunge i nuovi campi al database senza perdere i dati"""
    conn = sqlite3.connect(Config.DATABASE)
    cursor = conn.cursor()
    
    # Controlla se le colonne esistono già
    cursor.execute("PRAGMA table_info(anime_manga)")
    columns = [column[1] for column in cursor.fetchall()]
    
    # Aggiungi num_stagioni se non esiste
    if 'num_stagioni' not in columns:
        cursor.execute('ALTER TABLE anime_manga ADD COLUMN num_stagioni INTEGER DEFAULT 1')
        print("✅ Colonna 'num_stagioni' aggiunta")
    
    # Aggiungi episodi_per_stagione se non esiste
    if 'episodi_per_stagione' not in columns:
        cursor.execute('ALTER TABLE anime_manga ADD COLUMN episodi_per_stagione TEXT')
        print("✅ Colonna 'episodi_per_stagione' aggiunta")
    
    conn.commit()
    conn.close()
    print("✅ Database migrato correttamente!")

if __name__ == '__main__':
    migrate_database()
