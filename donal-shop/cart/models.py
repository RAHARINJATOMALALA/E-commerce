from django.db import models
from django.contrib.auth.models import User
from shop.models import Produit

class Panier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.utilisateur:
            return f"Panier de {self.utilisateur.username}"
        else:
            return f"Panier session {self.session_key}"
    
    def total(self):
        return sum(item.sous_total() for item in self.items.all())
    
    def nombre_articles(self):
        return sum(item.quantite for item in self.items.all())

class ArticlePanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, related_name='items')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
    
    def sous_total(self):
        return self.produit.prix * self.quantite