from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    """Connette al database SQLite"""
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Pagina principale - mostra tutti gli anime/manga"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM anime_manga ORDER BY data_aggiunta DESC')
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Pagina per aggiungere un nuovo anime/manga"""
    if request.method == 'POST':
        titolo = request.form['titolo']
        tipo = request.form['tipo']
        genere = request.form.get('genere', '')
        anno = request.form.get('anno', '')
        trama = request.form.get('trama', '')
        rating = request.form.get('rating', '')
        immagine_url = request.form.get('immagine_url', '')
        num_stagioni = request.form.get('num_stagioni', '')
        episodi_per_stagione = request.form.get('episodi_per_stagione', '')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO anime_manga (titolo, tipo, genere, anno, trama, rating, immagine_url, num_stagioni, episodi_per_stagione)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (titolo, tipo, genere, anno, trama, rating, immagine_url, num_stagioni, episodi_per_stagione))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/search')
def search():
    """Pagina di ricerca"""
    query = request.args.get('q', '')
    
    if query:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM anime_manga 
            WHERE titolo LIKE ? OR genere LIKE ? OR trama LIKE ?
            ORDER BY data_aggiunta DESC
        ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
        items = cursor.fetchall()
        conn.close()
    else:
        items = []
    
    return render_template('search.html', items=items, query=query)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    """Modifica un anime/manga"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        # Salva le modifiche
        titolo = request.form['titolo']
        tipo = request.form['tipo']
        genere = request.form.get('genere', '')
        anno = request.form.get('anno', '')
        trama = request.form.get('trama', '')
        rating = request.form.get('rating', '')
        immagine_url = request.form.get('immagine_url', '')
        num_stagioni = request.form.get('num_stagioni', '')
        episodi_per_stagione = request.form.get('episodi_per_stagione', '')
        
        cursor.execute('''
            UPDATE anime_manga 
            SET titolo = ?, tipo = ?, genere = ?, anno = ?, trama = ?, rating = ?, immagine_url = ?, num_stagioni = ?, episodi_per_stagione = ?
            WHERE id = ?
        ''', (titolo, tipo, genere, anno, trama, rating, immagine_url, num_stagioni, episodi_per_stagione, item_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    # GET - Mostra form precompilato
    cursor.execute('SELECT * FROM anime_manga WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    conn.close()
    
    if not item:
        return redirect(url_for('index'))
    
    return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    """Elimina un anime/manga dal database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM anime_manga WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    
    # Ritorna alla pagina precedente (homepage o ricerca)
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
