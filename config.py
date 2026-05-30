import os

class Config:
    """Configurazione base dell'applicazione"""
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
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
