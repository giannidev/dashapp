from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewMeasure(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_can_enter_a_measure(self):
        #Gianni wants to enter a new measure
        
        #He goes to his brand new webapp 
        self.browser.get('http://localhost:8000/')

        #He sees the message inviting to enter a new measure
        header_text = self.browser.find_element_by_tag_name('h1').text
        #body = self.browser.find_element_by_tag_name("body")
        #self.assert('dashapp' in body.text, "Did not find dashall in Body")
        self.assertIn(header_text,'Enter a new measure')
        
        #He is invited to enter new measure by entering a metric and a measure
        inputMetric = self.browser.find_element_by_id('id_new_metric')
        self.assertEqual(
            inputMetric.get_attribute('placeholder'),
            'Enter the metric'
        )
        inputMeasure = self.browser.find_element_by_id('id_new_measure')
        self.assertEqual(
            inputMeasure.get_attribute('placeholder'),
            'Enter the measure'
        )
        
        #He enters M1 to choose the metric
        inputMetric.send_keys('M1')
        #Then he hits TAB to go to the measure input
        inputMetric.send_keys(Keys.TAB)
        #And enters 10 as measure
        inputMeasure.send_keys('10')
        
        #When he hits enter the values are stored and showed in the recently entered list
        inputMetric.send_keys(Keys.ENTER)  
        time.sleep(5)
        
        recentTable = self.browser.find_element_by_id('id_recent_table')  
        rows = recentTable.find_elements_by_tag_name('tr')
        self.assertIn('M1: 10', [row.text for row in rows])
        #self.assertTrue(
         #   any(row.text == 'M1: 10' for row in rows),
         # f"New measure did not appear in table. Contents were:\n{recentTable.text}"            )
        
        self.fail('Finish the test!')
        
if __name__ == '__main__':
    unittest.main()