from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, current_user
from app.models import Projet, AnalyseTest

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@jwt_required()
def dashboard():
    # Récupère les projets ET les analyses de l'utilisateur
    projets = Projet.query.filter_by(id_utilisateur=current_user.id_utilisateur).all()
    analyses = AnalyseTest.query.filter_by(id_utilisateur=current_user.id_utilisateur).all()
    
    return render_template('dashboard.html', projets=projets, analyses=analyses)
