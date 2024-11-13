# Create your models here.

from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix_metre2 = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {
            "nom": self.nom,
            "code postale": self.code_postal,
            "prix par m2": self.prix_metre2,
        }


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville, on_delete=models.CASCADE
    )  # Composition ie une seule ville
    surface = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {
            "nom": self.nom,
            "ville": self.ville.json_extended(),
            "surface": self.surface,
        }


class SiegeSocial(Local):  # heritage siege herite de local
    def __str__(self):
        return f"Siege social a {self.ville.nom}"

    def json_extended(self):  # Rajout L
        return {
            "nom": self.nom,
            "ville": self.ville.json_extended(),
            "surface": self.surface,
        }


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    n_serie = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def costs(self):
        return self.prix

    def json_extended(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
            "numero de serie": self.n_serie,
        }


class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
        }


class Ressource(Objet):
    def __str__(self):
        return self.nom

    def json_extended(self):  # Rajout L
        return {
            "nom": self.nom,
            "prix": self.prix,
        }


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)  # composition
    quantite = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ressource.nom} : {self.quantite}"

    def costs(self):
        return self.quantite * self.ressource.prix

    def json_extended(self):  # Luc ajout
        return {
            "ressource": self.ressource.json_extended(),
            "quantite": self.quantite,
        }


class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField(default=0)
    etape_suivant = models.ForeignKey(
        "self", null=True, on_delete=models.PROTECT, blank=True
    )

    def __str__(self):
        return self.nom

    def json_extended(self):  # Luc ajout
        return {
            "nom": self.nom,
            "machine": self.machine.json_extended(),
            "quantite_ressource": self.quantite_ressource.json_extended(),
            "duree": self.duree,
            # M"etape_suivant" : self,   # A voir
        }


class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    def json_extended(self):  # Luc ajout
        return {
            "premiere_etape": self.premiere_etape.json_extended(),
        }


class Stock(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    nombre = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} x {self.ressource.nom}"

    def json_extended(self):
        return {
            "ressource": self.ressource.json_extended(),
            "nombre": self.nombre,
        }


class Usine(Local):  # heritage Usine herite de local
    machines = models.ManyToManyField(Machine)  # agrégation
    stock = models.ManyToManyField(Stock)  # je suppose qu'une usine à plusieurs stocks

    def __str__(self):
        return self.nom

    def costs(self):
        machine_cost = 0
        stock_cost = 0

        for mach in Machine.objects.all():
            machine_cost = machine_cost + mach.prix

        for stk in Stock.objects.all():
            stock_cost = stock_cost + stk.ressource.prix * stk.nombre

        local_cost = self.surface * self.ville.prix_metre2
        return machine_cost + stock_cost + local_cost

    def json_extended(self):
        return {
            "nom": self.nom,
            "ville": self.ville.json_extended(),
            "surface": self.surface,
            "machines": [mach.json_extended() for mach in self.machines.all()],
            "stock": [stoc.json_extended() for stoc in self.stock.all()],  # rajout L
        }
