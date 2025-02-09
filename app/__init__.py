from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation des extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Configuration des callbacks JWT
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id_utilisateur

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return db.session.get(Utilisateur, identity)

    # Enregistrement des blueprints
    from app.api.auth import auth_bp
    from app.api.dashboard import dashboard_bp
    from app.api.projet import projet_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(projet_bp)

    return app
