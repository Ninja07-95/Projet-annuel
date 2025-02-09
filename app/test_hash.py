import sys
import os

# Ajoutez le chemin du projet (répertoire racine) à sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import bcrypt
from app import create_app, db
from app.models import Utilisateur

app = create_app()

with app.app_context():
    utilisateurs = Utilisateur.query.all()
    for utilisateur in utilisateurs:
        if not utilisateur.mot_de_passe.startswith('$2b$'):  # Vérifie si le mot de passe n'est pas déjà hashé avec bcrypt
            utilisateur.set_password(utilisateur.mot_de_passe)  # Rehash le mot de passe avec bcrypt
            db.session.commit()
    print("Mots de passe rehashés avec succès.")
