import unittest
from app.services.prediction_service import PredictionService
from app.repositories.iris_repository import IrisRepository

class TestPredictionService(unittest.TestCase):
    def setUp(self):
        iris_repository = IrisRepository()
        self.prediction_service = PredictionService(iris_repository)

    def test_predict(self):
        sample_data = [5.1, 3.5, 1.4, 0.2]
        prediction = self.prediction_service.predict(sample_data)
        self.assertIn(prediction, [0, 1, 2])

if __name__ == '__main__':
    unittest.main()