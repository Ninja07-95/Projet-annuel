from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import auth, analysis, report


@api_bp.route('/')
def index():
    return "Bienvenue sur l'API Makkarriz !", 200
