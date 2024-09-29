# Create your tests here.
from django.test import TestCase
from .models import Machine

class MachineModelTests(TestCase):
  def test_machine_creation(self):
    self.assertEqual(Machine.objects.count(), 0)
    Machine.objects.create(nom="scie",prix=1_000,n_serie="16832")
    self.assertEqual(Machine.objects.count(), 1)
    Machine.objects.create(nom="tronconneuse",prix=2_000,n_serie="16831")
