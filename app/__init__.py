from flask import Flask
from app.models import db, migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stack.db'

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)

    from app.routes import main_bp
    app.register_blueprint(main_bp)
    

    return app

