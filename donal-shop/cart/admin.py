from django.contrib import admin
from .models import Panier, ArticlePanier

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'session_key', 'date_creation', 'total']
    list_filter = ['date_creation']

@admin.register(ArticlePanier)
class ArticlePanierAdmin(admin.ModelAdmin):
    list_display = ['panier', 'produit', 'quantite', 'sous_total']
    list_filter = ['panier']