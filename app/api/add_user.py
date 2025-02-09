import sys
import os
 #sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import Utilisateur

# Créer une instance de l'application Flask
app = create_app()

# Ajouter un utilisateur
with app.app_context():
    # Définir les informations de l'utilisateur
    nom = "Admin"
    email = "admin@example.com"
    role = "Admin"  # Options possibles : 'Admin', 'DevSecOps', 'Développeur'
    mot_de_passe = "password123"  # Mot de passe à hacher

    # Hacher le mot de passe
    hashed_password = generate_password_hash(mot_de_passe)

    # Créer une instance de l'utilisateur
    nouvel_utilisateur = Utilisateur(
        nom=nom,
        email=email,
        role=role,
        mot_de_passe=hashed_password
    )

    # Ajouter et sauvegarder dans la base de données
    db.session.add(nouvel_utilisateur)
    db.session.commit()
    print(f"Utilisateur ajouté avec succès : {email}")
