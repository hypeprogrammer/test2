# app/services/prediction_service.py
class PredictionService:
    def __init__(self, iris_repository):
        self.iris_repository = iris_repository

    def predict(self, data):
        model = self.iris_repository.load_model()
        prediction = model.predict([data])
        return prediction[0]