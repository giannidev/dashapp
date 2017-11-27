# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import resolve
from dashapp.views import home_page
from django.http import HttpRequest
from dashapp.models import Metric, Measure, Event
from datetime import date

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
        
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_root_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    '''obsolete def test_can_save_a_metric_in_POST_request(self):
        response = self.client.post('/', data={'new_metric': 'A new metric',
                                               'new_measure': 'A new measure'})
        self.assertEqual(Metric.objects.count(), 1)
        new_metric = Metric.objects.first()
        self.assertEqual(new_metric.name,'A new metric')
        '''
        
    def test_can_create_an_event(self):
         newEvent = Event.objects.create(name='dummy event', date=date.today())
         self.assertEqual(Event.objects.count(),1,'Expecting 1 but got '+str(Event.objects.count()))
         
        
    def test_redirect_after_POST(self):
        Metric.objects.create(name='M1', description="first metric", frequence="RELEASE")
        Metric.objects.create(name='M2', description="second metric", frequence="RELEASE")
        
        response = self.client.post('/', data={'new_event_name': 'dummy',
                                               'new_measure_M1': '10',
                                               'new_measure_M2': '20'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
        
    def test_only_saves_metrics_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Metric.objects.count(), 0)
        
    '''   def test_displays_all_metrics(self):
        Metric.objects.create(name='M1')
        Metric.objects.create(name='M2')

        response = self.client.get('/')

        self.assertIn('M1', response.content.decode())
        self.assertIn('M2', response.content.decode())
    '''
        
    def test_displays_all_full_metrics(self):
        Metric.objects.create(name='M1', description="first metric", frequence="RELEASE")
        Metric.objects.create(name='M2', description="second metric", frequence="RELEASE")

        response = self.client.get('/')

        self.assertIn('M1 first metric RELEASE', response.content.decode())
        self.assertIn('M2 second metric RELEASE', response.content.decode())
        
    def test_displays_only_RELEASE_metrics_and_full(self):
        Metric.objects.create(name='M1', description="first metric", frequence="RELEASE")
        Metric.objects.create(name='M2', description="second metric", frequence="MONTH")
        Metric.objects.create(name='M3', description="third metric", frequence="RELEASE")
        Metric.objects.create(name='M4', description="third metric", frequence="MONTH")
        response = self.client.get('/')

        self.assertIn('M1 first metric RELEASE', response.content.decode())
        self.assertIn('M3 third metric RELEASE', response.content.decode())
        self.assertNotIn('M2 second metric MONTH', response.content.decode())
        
    def test_homepage_returns_all_the_release_metrics_with_input(self):
        Metric.objects.create(name='M1', description="first metric", frequence="RELEASE")
        Metric.objects.create(name='M3', description="third metric", frequence="RELEASE")
        response = self.client.get('/')

        self.assertIn('M1 first metric RELEASE', response.content.decode())
        self.assertIn('id_new_measure_M1', response.content.decode())
        self.assertIn('M3 third metric RELEASE', response.content.decode())
        self.assertIn('id_new_measure_M3', response.content.decode())
        
    def test_store_new_release_measures(self):
        Metric.objects.create(name='M1', description="first metric", frequence="RELEASE", modifier=1)
        Metric.objects.create(name='M2', description="second metric", frequence="MONTH", modifier=1)
        Metric.objects.create(name='M3', description="third metric", frequence="RELEASE", modifier=2)
        
        response = self.client.post('/', data={'new_event_name':'dummy event',
                                               'new_measure_M1': '10',
                                               'new_measure_M2': '20'})
        
        self.assertEqual(Measure.objects.count(), 2)
        firstMeasure = Measure.objects.first()
        self.assertEqual(firstMeasure.metric,Metric.objects.first())
        self.assertEqual(firstMeasure.value,10)
        secondMeasure = Measure.objects.last()
        self.assertEqual(secondMeasure.metric,Metric.objects.last())
        self.assertEqual(secondMeasure.value,10)


class MetricModelTest(TestCase):

    def test_can_calculate_value_with_modifier(self):
        mymetric = Metric.objects.create(name='M1', description="first metric", frequence="RELEASE", modifier=2)
        myevent = Event.objects.create(name='dummy event', date=date.today())
        mymeasure = Measure.objects.create(metric=mymetric, event=myevent, rawValue=20)
        self.assertEqual(mymeasure.value,10)
        
    
    def test_saving_and_retrieving_metrics(self):
        first_metric = Metric()
        first_metric.name = 'M1'
        first_metric.description = 'Description for M1'
        first_metric.frequence = "MONTH"
        first_metric.save()

        second_metric = Metric.objects.create(name='M2',description='Description for M2',frequence='RELEASE')
       # second_metric.name = 'M2'
       # second_metric.description = 'Description for M2'
       # second_metric.frequence = "RELEASE"
       # second_metric.save()

        saved_items = Metric.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'M1')
        self.assertEqual(second_saved_item.description, 'Description for M2')
        
        
        