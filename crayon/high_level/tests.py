# Create your tests here.
from django.test import TestCase
from .models import Ville, Machine, Usine, QuantiteRessource, Ressource, Stock


class UsineCostModelTests(TestCase):
    def test_usine_creation(self):
        self.ville = Ville.objects.create(
            nom="Toulouse", code_postal=31000, prix_metre2=2000
        )
        self.usine = Usine.objects.create(nom="Dopron", ville="Toulouse", surface=50)
        self.machine_1 = Machine.objects.create(
            nom="Bras robot", prix=2000, n_serie=17896
        )
        self.machine_2 = Machine.objects.create(
            nom="Bras robot", prix=1000, n_serie=15732
        )

        self.objet1 = Ressource.objects.create(nom="Bois", prix=10)
        self.objet2 = Ressource.objects.create(nom="Mine", prix=15)
        self.stock = Stock.objects.create(ressource=self.objet1, nombre=1000)
        self.stock = Stock.objects.create(ressource=self.objet2, nombre=50)

    def Calcul_cout_usine(self):
        usineCost = self.usine.costs()
        machine_cost = 2000 + 1000
        surface_cost = 2000 * 50
        total_cost = machine_cost + surface_cost

        self.assertEqual(usineCost, total_cost)

    def Calcul_cout_quantiteRessource(self):
        quantite_bois = QuantiteRessource.objects.get(ressource=self.objet1)
        quantite_mine = QuantiteRessource.objects.get(ressource=self.objet2)

        bois_cost = quantite_bois.costs()
        mine_cost = quantite_mine.costs()

        bois_cost_attendu = 10000
        mine_cost_attendu = 750

        self.assertEqual(bois_cost, bois_cost_attendu)
        self.assertEqual(mine_cost, mine_cost_attendu)
