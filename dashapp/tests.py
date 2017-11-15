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
        
    '''def test_assert_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.strip().endswith('</html>'))
      '''  
    '''def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)
        '''
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'home.html')  