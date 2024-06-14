import unittest
import json
from main import app

class TestPredictionEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        response = self.app.post('/api/predict',
                                 data=json.dumps({"features": [5.1, 3.5, 1.4, 0.2]}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('prediction', data)
        self.assertIn(data['prediction'], [0, 1, 2])

if __name__ == '__main__':
    unittest.main()