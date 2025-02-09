from app import db
import bcrypt

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    __table_args__ = {'extend_existing': True}

    id_utilisateur = db.Column(db.BigInteger, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(191), nullable=False, unique=True)
    role = db.Column(db.Enum('Admin', 'DevSecOps', 'Développeur'), nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    date_creation = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    analyses = db.relationship('AnalyseTest', backref='utilisateur', lazy=True)
    projets = db.relationship('Projet', backref='auteur', lazy=True)

    def set_password(self, password):
        self.mot_de_passe = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.mot_de_passe.encode('utf-8'))

class Projet(db.Model):
    __tablename__ = 'projet'
    __table_args__ = {'extend_existing': True}
    
    id_projet = db.Column(db.BigInteger, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    date_scan = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    id_utilisateur = db.Column(db.BigInteger, db.ForeignKey('utilisateur.id_utilisateur'))

class AnalyseTest(db.Model):
    __tablename__ = 'analyse_test'
    __table_args__ = {'extend_existing': True}
    
    id_analyse = db.Column(db.BigInteger, primary_key=True)
    langage = db.Column(db.Enum('PHP', 'Python', 'Rust'), nullable=False)
    date_analyse = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    id_utilisateur = db.Column(db.BigInteger, db.ForeignKey('utilisateur.id_utilisateur'))
    id_projet = db.Column(db.BigInteger, db.ForeignKey('projet.id_projet'))
    chemin_fichier = db.Column(db.String(255), nullable=False)

# ... (Vulnerabilite, Rapport, Historique restent identiques)
class Vulnerabilite(db.Model):
    __tablename__ = 'vulnerabilite'
    __table_args__ = {'extend_existing': True}
    
    id_vulnerabilite = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.Enum('SQL Injection', 'XSS', 'Path Traversal', 'RCE'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    fichier = db.Column(db.String(255), nullable=False)
    ligne_code = db.Column(db.Integer, nullable=False)
    id_analyse = db.Column(db.BigInteger, db.ForeignKey('analyse_test.id_analyse'))

class Rapport(db.Model):
    __tablename__ = 'rapport'
    __table_args__ = {'extend_existing': True}
    
    id_rapport = db.Column(db.BigInteger, primary_key=True)
    format = db.Column(db.Enum('PDF', 'JSON', 'XML', 'HTML'), nullable=False)
    chemin_fichier = db.Column(db.String(255), nullable=False)
    id_analyse = db.Column(db.BigInteger, db.ForeignKey('analyse_test.id_analyse'))

class Historique(db.Model):
    __tablename__ = 'historique'
    __table_args__ = {'extend_existing': True}
    
    id_historique = db.Column(db.BigInteger, primary_key=True)
    id_utilisateur = db.Column(db.BigInteger, db.ForeignKey('utilisateur.id_utilisateur'))
    action = db.Column(db.Text, nullable=False)
    date_action = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
