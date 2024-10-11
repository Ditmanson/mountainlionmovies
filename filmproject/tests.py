from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone
from django.urls import reverse, resolve

# 1st test to make sure our testing environment is working
class SimpleTest(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)