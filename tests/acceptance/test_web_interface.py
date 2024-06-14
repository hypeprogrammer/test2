import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebInterface(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is installed and added to PATH

    def test_prediction_form(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/api/predict_form")

        sepal_length = driver.find_element_by_name("sepal_length")
        sepal_width = driver.find_element_by_name("sepal_width")
        petal_length = driver.find_element_by_name("petal_length")
        petal_width = driver.find_element_by_name("petal_width")

        sepal_length.send_keys("5.1")
        sepal_width.send_keys("3.5")
        petal_length.send_keys("1.4")
        petal_width.send_keys("0.2")
        petal_width.send_keys(Keys.RETURN)

        self.assertIn("The predicted class is:", driver.page_source)
        self.assertIn("0", driver.page_source)  # Assuming class 0 for the given input

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()