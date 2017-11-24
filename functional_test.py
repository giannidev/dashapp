from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.remote.webelement import WebElement

class NewMeasures(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def inputMeasure(self, metric, measure):
        inputMeasure = self.browser.find_element_by_id('id_new_measure_' + metric)
        self.assertEqual(
            inputMeasure.get_attribute('placeholder'),
            'Enter the measure'
        )
        inputMeasure.send_keys(measure)

    def test_can_enter_release_measures(self):
        #Given two metrics stored in the DB
        #When I enter release metrics
        #Then this metrics are correctly saved in the database
       
        
        #He goes to his brand new webapp 
        self.browser.get('http://localhost:8000/')

        #He sees the message inviting to enter a new measure
        header_text = self.browser.find_element_by_tag_name('h1').text
        #body = self.browser.find_element_by_tag_name("body")
        #self.assert('dashapp' in body.text, "Did not find dashall in Body")
        self.assertIn(header_text,'NEW Release Measures')
        
        #He enters two measures
        self.inputMeasure('M1', '10')
        self.inputMeasure('M2', '20')
        self.browser.find_element_by_name('submit').click()
        
        '''#The measures are stored in the db
        self.assertEqual(Measure.objects.count(), 2)
        firstMeasure = Measure.objects.first()
        self.assertEqual(firstMeasure.metric,Metric.objects.first())
        self.assertEqual(firstMeasure.rawValue,10)
        secondMeasure = Measure.objects.last()
        self.assertEqual(secondMeasure.metric,Metric.objects.last())
        self.assertEqual(secondMeasure.rawValue,20)
        '''
        
        
if __name__ == '__main__':
    unittest.main()