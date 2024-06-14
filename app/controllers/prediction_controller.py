from flask import Blueprint, request, jsonify, render_template
from app.services.prediction_service import PredictionService
from app.repositories.iris_repository import IrisRepository

prediction_bp = Blueprint('prediction_bp', __name__)
iris_repository = IrisRepository()
prediction_service = PredictionService(iris_repository)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = prediction_service.predict(data['features'])
    return jsonify({'prediction': int(prediction)})

@prediction_bp.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    if request.method == 'POST':
        features = [float(request.form['sepal_length']),
                    float(request.form['sepal_width']),
                    float(request.form['petal_length']),
                    float(request.form['petal_width'])]
        prediction = prediction_service.predict(features)
        return render_template('result.html', prediction=prediction)
