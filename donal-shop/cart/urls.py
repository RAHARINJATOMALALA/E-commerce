from django.urls import path
from . import views

urlpatterns = [
    path('', views.voir_panier, name='voir_panier'),
    path('ajouter/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('modifier/<int:article_id>/', views.modifier_quantite, name='modifier_quantite'),
    path('supprimer/<int:article_id>/', views.supprimer_article, name='supprimer_article'),
]