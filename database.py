from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer les variables d'environnement
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_DATABASE")

# Vérification des variables
if not all([DB_USERNAME, DB_HOST, DB_PORT, DB_NAME]):
    raise ValueError("Missing one or more database environment variables. Check your .env file.")

# Créer l'URL de connexion MySQL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Initialiser le moteur SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Créer une session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir la classe de base pour SQLAlchemy
Base = declarative_base()

# Fonction pour récupérer une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
