from flask import Flask
from app.controllers.prediction_controller import prediction_bp
from app.controllers.main_controller import main_bp

app = Flask(__name__)
app.register_blueprint(prediction_bp, url_prefix='/api')
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)