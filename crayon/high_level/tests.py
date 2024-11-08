# Create your tests here.
from django.test import TestCase
from .models import Ville, Machine, Ressource, Usine, Stock


class TestUnitaire(TestCase):
    def test_usine_creation(self):
        ville = Ville.objects.create(nom="Labege", code_postal=31000, prix_metre2=2000)

        machine1 = Machine.objects.create(nom="M1", prix=1000, n_serie=16832)
        machine2 = Machine.objects.create(nom="M2", prix=2000, n_serie=16833)

        usine1 = Usine.objects.create(nom="EtsIndustries", ville=ville, surface=50)

        usine1.machines.set([machine1, machine2])

        bois = Ressource.objects.create(nom="bois", prix=10)
        mine = Ressource.objects.create(nom="mine", prix=15)

        # quantite_bois = QuantiteRessource.objects.create( ressource=bois, quantite=1000)
        # quantite_mine = QuantiteRessource.objects.create(ressource=mine, quantite=50)

        stock_bois = Stock.objects.create(ressource=bois, nombre=1000)
        stock_mine = Stock.objects.create(ressource=mine, nombre=50)

        usine1.stock.set([stock_bois, stock_mine])

        # total_cout = usine1.costs() + quantite_bois.costs() + quantite_mine.costs()
        self.assertEqual(Usine.objects.first().costs(), 110750)
