from django.test import TestCase
import requests
from datetime import datetime, timezone
import json
from random import random, seed


# Create your tests here.
class MeasurementTest(TestCase):
    url = 'http://localhost:8000/api/v1/measurement/'
    auth=('theo','Heinis14')
    headers= {
        "content-type": "application/json",
    }
    
    def post(self,data):
        return requests.post(
            self.url,
            headers=self.headers,
            auth=self.auth,
            data=json.dumps(data,default=lambda d: d.isoformat()))
    
    def get(self):
        return requests.get(
            self.url,
            auth=self.auth,
            headers=self.headers)
        
    def setUp(self):
        seed()
        TestCase.setUp(self)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_list(self):
        response = self.get()
        response.raise_for_status()
        
    def test_post_single(self):
        data = {
            "location": {"type": "Point","coordinates": [4+random(), 52+random()]},
            "time": datetime.now(timezone.utc),
            "parameter": "temperature",
            "unit": "°C",
            "value": round(6.5 + random(),2)
        }
        response = self.post(data)
        response.raise_for_status()

    def test_post_many(self):
        data = [
        {
            "location": {"type": "Point","coordinates": [4+random(), 52+random()]},
            "time": datetime.now(timezone.utc),
            "parameter": "temperature",
            "unit": "°C",
            "value": round(6.5 + random(),2)
        }
            for i in range(0,10000)
        ]
        response = self.post(data)
        response.raise_for_status()
        