from django.contrib import admin
from .models import Categorie, Produit

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']
    search_fields = ['nom']

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'categorie', 'en_stock', 'date_creation']
    list_filter = ['categorie', 'en_stock', 'date_creation']
    search_fields = ['nom', 'description']
    list_editable = ['prix', 'en_stock']