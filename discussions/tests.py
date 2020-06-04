from django.test import TestCase
from rest_framework.test import APITestCase
from discussions.models import Discussion
import os
from django.conf import settings


# Tests for REST API
class DiscussionCreateTestCase(APITestCase):
    def test_create_discussion(self):
        discussion_attrs = {
            'title': 'New title',
            'content': 'This is a content.',
            'img': '/home/vijay/Downloads/kathmandu-pollution.jpg',
            'user': '1',

        }
        response = self.client.post('/api-discussion/new', discussion_attrs)
        if response.status_code != 201:
            print(response.data)