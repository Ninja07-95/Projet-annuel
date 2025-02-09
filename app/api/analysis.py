from flask import jsonify, request
from app.models import AnalyseTest
from app import db
from app.api import api_bp

@api_bp.route('/analysis', methods=['POST'])
def create_analysis():
    data = request.json
    langage = data.get('langage')
    chemin_fichier = data.get('chemin_fichier')
    id_utilisateur = data.get('id_utilisateur')

    analyse = AnalyseTest(
        langage=langage,
        chemin_fichier=chemin_fichier,
        id_utilisateur=id_utilisateur
    )
    db.session.add(analyse)
    db.session.commit()

    return jsonify(message="Analyse créée avec succès", id_analyse=analyse.id_analyse), 201
