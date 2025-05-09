# Inspire-Hub-API-

# FastAPI Project

## Installation et exécution

### Prérequis
- Python 3.9+
- MySQL
- pip (gestionnaire de paquets Python)

### Étapes d'installation
1. **Télécharger le projet**
   
2. **Créer un environnement virtuel puis l'activer** 
   python -m venv venv
   # Sur Windows : venv\Scripts\activate
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
  

3. **Installer les dépendances**
   
   pip install -r requirements.txt
   ```

4. **Configurer la base de données MySQL**
   utiliser un logiciel comme WAMPSERVER pour la base de données MySQL
    
   - Mettez à jour le fichier `.env` avec les informations de connexion :
     ```
     DB_HOST=localhost
     DB_PORT=3306
     DB_USER=root
     DB_PASSWORD=yourpassword
     DB_NAME=

5. **Exécuter les migrations de base de données** 
(utilisez SQLAlchemy et Alembic)
   

6. **Lancer le serveur**
  bash
  fastapi dev main.py
   ```
   L'API sera disponible sur : `http://127.0.0.1:8000`

## Test des Endpoints avec Insomnia

### Tester avec Insomnia
1. Ouvrir Insomnia.
2. Aller dans **Application > Importer > Fichier inspire_hub.json**.
3. Sélectionner le fichier 
4. Exécuter les requêtes disponibles.

## Documentation de l'API
FastAPI fournit une documentation  :
- Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## Licence
Ce projet est sous licence MIT.
