# Create your views here.

from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import DetailView
from .models import (
    Ville,
    Local,
    Machine,
    Usine,
)  # ,SiegeSocial,Machine,Objet,Ressource,QuantiteRessource,Stock,Etape,Produit
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


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json())
