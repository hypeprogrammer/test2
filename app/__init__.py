from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.controllers.prediction_controller import prediction_bp
    app.register_blueprint(prediction_bp, url_prefix='/api')

    return app