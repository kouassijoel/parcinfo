from django.test import TestCase
from .models import *

# Create your tests here.

class Suppression(TestCase):
    def test_delete(self):
        ressource = Restitution.objects.create(description="bonjour")
        ressource.delete()
