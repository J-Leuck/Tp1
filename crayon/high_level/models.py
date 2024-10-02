# Create your models here.

from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix_metre2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} \n {self.code_postal}"

    def json_extended(self):
        return {
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prix_metre2": self.prix_metre2,
        }


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville, on_delete=models.CASCADE
    )  # Composition ie une seule ville
    surface = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} \n {self.ville}"

    def json(self):
        return {
            "nom": self.nom,
            "ville": self.ville.json_extended(),
            "surface": self.surface,
        }


class SiegeSocial(Local):  # heritage siege herite de local
    def __str__(self):
        return f"Siège social à {self.ville.nom}"


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    n_serie = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} : {self.n_serie}"

    def costs(self):
        return self.prix

    def json_extended(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
            "n_serie": self.n_serie,
        }


class Usine(Local):  # heritage Usine herite de local
    machines = models.ManyToManyField(Machine)  # agrégation

    def __str__(self):
        return self.nom

    def costs(self):
        machine_cost = 0
        for mach in Machine.objects.all():
            machine_cost = machine_cost + mach.prix

        local_cost = self.surface * self.ville.prix_metre2
        return machine_cost + local_cost

    def json(self):
        return {
            "nom": self.nom,
            "ville": {
                "nom": self.ville.nom,
                "code_postale": self.ville.code_postal,
                "prix": self.ville.prix_metre2,
            },
            "surface": self.surface,
            "machines": [
                mach.json_extended() for mach in self.machines.all()
            ],  # [mach.pk for mach in Machine.objects.all()
            # ],
        }


# list.append(mach.id)


class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} \n {self.prix} $"


"""    def json(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
        }"""


class Ressource(Objet):
    def __str__(self):
        return self.nom


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)  # composition
    quantite = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ressource.nom} : {self.quantite}"

    def costs(self):
        return self.quantite * self.ressource.prix


"""    def json(self):
        return {
            "ressource": {
                "nom": self.ressource.nom,
                "prix": self.ressource.prix,
            },
            "quantite": self.quantite,
        }"""


class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField(default=0)
    etape_suivant = models.ForeignKey(
        "self", null=True, on_delete=models.PROTECT, blank=True
    )

    def __str__(self):
        return f"{self.nom} : {self.machine.nom} \n {self.duree}"


"""    def json(self):
        return {
            "nom": self.nom,
            "machine": {
                "nom": self.machine.nom,
                "prix": self.machine.prix,
                "n_serie": self.machine.n_serie,
            },
            "quantite_ressource": {
                "ressource": self.quantite_ressource.ressource,
                "quantite": self.quantite_ressource.quantite,
            },
            "duree": self.duree,
             "etape_suivante": self

        }"""


class Produit(Objet):
    premiere_etape = models.ForeignKey(
        Etape, null=True, on_delete=models.PROTECT, blank=True
    )

    def __str__(self):
        return f"{self.nom} "


"""    def json(self):
        return {
            "Etape": {
                "nom": self.premiere_etape.nom,
                "machine": self.premiere_etape.machine,
                "quantite_ressource": self.premiere_etape.quantite_ressource,
                "duree": self.premiere_etape.duree,
            }
            # if self.premiere_etape
            # else None,
        }"""


class Stock(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    nombre = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ressource.nom} : {self.nombre}"

    """def json(self):
        return {
            "ressource": {
                "nom": self.ressource.nom,
                "prix": self.ressource.prix,
            },
            "nombre": self.nombre,
        }"""
