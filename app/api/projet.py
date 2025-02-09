from flask import Blueprint, request, redirect, render_template
from flask_jwt_extended import jwt_required, current_user
from app.models import Projet, AnalyseTest, db

projet_bp = Blueprint('projet', __name__)

@projet_bp.route('/creer-projet', methods=['GET', 'POST'])
@jwt_required()
def creer_projet():
    if request.method == 'POST':
        nom_projet = request.form.get('nom')
        fichier = request.files.get('fichier')
        
        # Enregistrez le fichier quelque part (ex: dossier uploads/)
        chemin_fichier = f"uploads/{fichier.filename}"
        fichier.save(chemin_fichier)
        
        # Créez le projet et l'analyse
        nouveau_projet = Projet(
            nom=nom_projet,
            id_utilisateur=current_user.id_utilisateur
        )
        db.session.add(nouveau_projet)
        db.session.commit()
        
        nouvelle_analyse = AnalyseTest(
            langage="Python",  # Déterminez le langage dynamiquement
            chemin_fichier=chemin_fichier,
            id_utilisateur=current_user.id_utilisateur,
            id_projet=nouveau_projet.id_projet
        )
        db.session.add(nouvelle_analyse)
        db.session.commit()
        
        return redirect('/dashboard')
    
    return render_template('creer_projet.html')
