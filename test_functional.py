import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class AllTests(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)

    def test_user_can_loging(self):
        self.driver.get("http://localhost:5000")
        self.driver.find_element_by_id("name").send_keys("devops")
        self.driver.find_element_by_id("password").send_keys("qwe123qwe")
        self.driver.find_element_by_id("loginbutton").click()
        print(self.driver.current_url)
        self.assertIn('http://localhost:5000/courses', self.driver.current_url)
        assert "No results found." not in self.driver.page_source

if __name__ == "__main__":
    unittest.main()
