from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('categorie/<int:categorie_id>/', views.produits_par_categorie, name='produits_categorie'),
]