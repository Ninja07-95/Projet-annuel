from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token
from app.models import Utilisateur, AnalyseTest, Vulnerabilite, Rapport, Historique
from app import db

api_bp = Blueprint('api', __name__)

from werkzeug.security import check_password_hash

@api_bp.route('/auth', methods=['POST'])
def authenticate():
    data = request.json
    email = data.get('email')
    mot_de_passe = data.get('mot_de_passe')

    utilisateur = Utilisateur.query.filter_by(email=email).first()
    if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
        token = create_access_token(identity=utilisateur.id_utilisateur)
        return jsonify(access_token=token), 200
    else:
        return jsonify(message="Email ou mot de passe incorrect"), 401

@api_bp.route('/analyse', methods=['POST'])
@jwt_required()
def create_analyse():
    data = request.json
    langage = data.get('langage')
    chemin_fichier = data.get('chemin_fichier')
    id_utilisateur = data.get('id_utilisateur')

    nouvelle_analyse = AnalyseTest(langage=langage, chemin_fichier=chemin_fichier, id_utilisateur=id_utilisateur)
    db.session.add(nouvelle_analyse)
    db.session.commit()

    return jsonify(message="Analyse créée avec succès", id_analyse=nouvelle_analyse.id_analyse), 201


@api_bp.route('/analyses', methods=['GET'])
@jwt_required()
def get_analyses():
    analyses = AnalyseTest.query.all()
    return jsonify([{
        'id_analyse': analyse.id_analyse,
        'langage': analyse.langage,
        'chemin_fichier': analyse.chemin_fichier,
        'date_analyse': analyse.date_analyse
    } for analyse in analyses])





from flask_restx import Api

api = Api(app, doc='/docs', title="Makkarriz API", description="Documentation interactive")
