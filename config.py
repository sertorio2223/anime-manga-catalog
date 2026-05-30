import os

class Config:
    """Configurazione base dell'applicazione"""
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Su Vercel (produzione) usa /tmp per il database, altrimenti la directory locale
    if os.environ.get('VERCEL'):
        DATABASE = '/tmp/database.db'
    else:
        DATABASE = os.path.join(BASE_DIR, 'database.db')
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-123'
    DEBUG = False

class DevelopmentConfig(Config):
    """Configurazione per sviluppo locale"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurazione per Vercel"""
    DEBUG = False

# Usa DevelopmentConfig di default
config = DevelopmentConfig
