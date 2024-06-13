from flask import Flask
from app.controllers.prediction_controller import prediction_bp

app = Flask(__name__)
app.register_blueprint(prediction_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)