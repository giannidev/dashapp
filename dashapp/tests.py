# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import resolve
from dashapp.views import home_page
from django.http import HttpRequest

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
        
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'new_metric': 'A new metric'})
        self.assertIn('A new metric', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')