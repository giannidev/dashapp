from selenium import webdriver
import unittest

class NewMeasure(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_can_enter_a_measure(self):
        #User can enter a new measure
        self.browser.get('http://localhost:8000/dashapp')

        #assert 'dashapp' in browser.find_elements(by, value)
        body = self.browser.find_element_by_tag_name("body")
        self.assert_('dashapp' in body.text, "Did not find dashall in Body")
        self.fail('Finish the test!')
        
if __name__ == '__main__':
    unittest.main()