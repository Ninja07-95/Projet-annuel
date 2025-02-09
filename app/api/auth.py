from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
from app.models import Utilisateur

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def authenticate():
    try:
        data = request.get_json()
        email = data.get('email')
        mot_de_passe = data.get('mot_de_passe')

        if not email or not mot_de_passe:
            return jsonify(error="Email et mot de passe requis"), 400

        utilisateur = Utilisateur.query.filter_by(email=email).first()
        
        if utilisateur and utilisateur.check_password(mot_de_passe):
            token = create_access_token(identity=utilisateur)
            return jsonify(access_token=token), 200
        else:
            return jsonify(error="Identifiants invalides"), 401
            
    except Exception as e:
        return jsonify(error=str(e)), 500

@auth_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')
