from flask import Flask
from app.common.config import Config
from app.models.producto import db
from app.controller.product_controller import product_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    CORS(app)

    # Registrar los Blueprints (Controladores)
    app.register_blueprint(product_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas en MySQL automáticamente si no existen
    app.run(debug=True, port=5000)