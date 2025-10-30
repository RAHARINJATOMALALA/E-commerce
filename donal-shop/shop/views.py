from django.shortcuts import render, get_object_or_404
from .models import Produit, Categorie

def accueil(request):
    produits = Produit.objects.filter(en_stock=True)[:8]
    return render(request, 'accueil.html', {'produits': produits})

def liste_produits(request):
    produits = Produit.objects.filter(en_stock=True)
    return render(request, 'produits/liste.html', {'produits': produits})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id, en_stock=True)
    return render(request, 'produits/detail.html', {'produit': produit})

def produits_par_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    produits = Produit.objects.filter(categorie=categorie, en_stock=True)
    return render(request, 'produits/categorie.html', {
        'categorie': categorie,
        'produits': produits
    })