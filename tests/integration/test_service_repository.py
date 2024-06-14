import unittest
from app.services.prediction_service import PredictionService
from app.repositories.iris_repository import IrisRepository

class TestServiceRepositoryIntegration(unittest.TestCase):
    def setUp(self):
        self.iris_repository = IrisRepository()
        self.prediction_service = PredictionService(self.iris_repository)

    def test_service_repository_interaction(self):
        sample_data = [5.1, 3.5, 1.4, 0.2]
        model = self.iris_repository.load_model()
        prediction = self.prediction_service.predict(sample_data)
        expected_prediction = model.predict([sample_data])[0]
        self.assertEqual(prediction, expected_prediction)

if __name__ == '__main__':
    unittest.main()