from flask import Flask

def create_app():
    app = Flask(__name__)

    # 여기에 필요한 Flask 설정을 추가할 수 있습니다.
    # 예: app.config['SECRET_KEY'] = 'your_secret_key'

    # 블루프린트 등록
    from app.controllers.prediction_controller import prediction_bp
    app.register_blueprint(prediction_bp, url_prefix='/api')

    return app