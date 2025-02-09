from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.models import Rapport
from app import db
from app.api import api_bp

@api_bp.route('/rapports', methods=['POST'])

#@jwt_required()
def create_rapport():
    data = request.json
    format_rapport = data.get('format')
    chemin_fichier = data.get('chemin_fichier')
    id_analyse = data.get('id_analyse')

    nouveau_rapport = Rapport(format=format_rapport, chemin_fichier=chemin_fichier, id_analyse=id_analyse)
    db.session.add(nouveau_rapport)
    db.session.commit()

    return jsonify(message="Rapport créé avec succès", id_rapport=nouveau_rapport.id_rapport), 201
