# Create your views here.

from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import DetailView
from .models import (
    Ville,
    Local,
    Usine,
    Machine,
    Objet,
    SiegeSocial,
    Ressource,
    QuantiteRessource,
    Etape,
    Produit,
    Stock,
)
from django.http import JsonResponse


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class LocalDetailView(DetailView):
    model = Local

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json())


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class ObjetDetailView(DetailView):
    model = Objet

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json())


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class SiegeSocialDetailView(DetailView):
    model = SiegeSocial

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json())


class RessourceDetailView(DetailView):
    model = Ressource

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json())


class QuantiteRessourceDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class EtapeDetailView(DetailView):
    model = Etape

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class StockDetailView(DetailView):
    model = Stock

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())
