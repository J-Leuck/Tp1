# Create your tests here.
from django.test import TestCase
from .models import Ville, Machine, Usine, QuantiteRessource, Ressource


class UsineCostModelTests(TestCase):
    def test_usine_creation(self):
        self.ville = Ville.objects.create(
            nom="Toulouse", code_postal=31000, prix_metre2=2000
        )
        self.usine = Usine.objects.create(nom="Dopron", ville=self.ville, surface=50)
        self.machine_1 = Machine.objects.create(
            nom="Bras robot", prix=2000, n_serie=17896
        )
        self.machine_2 = Machine.objects.create(
            nom="Bras robot", prix=1000, n_serie=15732
        )
        self.usine.machines.set([self.machine_1, self.machine_2])

        objet1 = Ressource.objects.create(nom="Bois", prix=10)
        objet2 = Ressource.objects.create(nom="Mine", prix=15)
        # stock = Stock.objects.create(ressource=objet1, nombre=1000)
        # stock = Stock.objects.create(ressource=objet2, nombre=50)

        # def test_Calcul_cout_usine(self):
        usineCost = self.usine.costs()
        machine_cost = 2000 + 1000
        surface_cost = 2000 * 50
        total_cost = machine_cost + surface_cost

        self.assertEqual(usineCost, total_cost)

        # def test_Calcul_cout_quantiteRessource(self):
        quantite_bois = QuantiteRessource.objects.create(
            ressource=objet1, quantite=1000
        )
        quantite_mine = QuantiteRessource.objects.create(ressource=objet2, quantite=50)

        bois_cost = quantite_bois.costs()
        mine_cost = quantite_mine.costs()
        total_produit = bois_cost + mine_cost

        bois_cost_attendu = 10000
        mine_cost_attendu = 750
        # total_produit_attendu = bois_cost_attendu + mine_cost_attendu

        self.assertEqual(bois_cost, bois_cost_attendu)
        self.assertEqual(mine_cost, mine_cost_attendu)

        # def test_Calcul_cout_total(self):
        cout_total = usineCost + total_produit

        cout_total_attendu = 0  # self.total_cost + self.total_produit_attendu

        self.assertEqual(cout_total, cout_total_attendu)
