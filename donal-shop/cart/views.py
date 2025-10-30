from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Panier, ArticlePanier
from shop.models import Produit
import uuid

def get_panier(request):
    """Récupère ou crée un panier pour l'utilisateur ou la session"""
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        panier, created = Panier.objects.get_or_create(session_key=session_key)
    return panier

def ajouter_au_panier(request, produit_id):
    """Ajoute un produit au panier"""
    produit = get_object_or_404(Produit, id=produit_id)
    panier = get_panier(request)
    
    # Vérifier si le produit est déjà dans le panier
    article, created = ArticlePanier.objects.get_or_create(
        panier=panier,
        produit=produit,
        defaults={'quantite': 1}
    )
    
    if not created:
        article.quantite += 1
        article.save()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': 'Produit ajouté au panier',
            'nombre_articles': panier.nombre_articles()
        })
    
    return redirect('voir_panier')

def voir_panier(request):
    """Affiche le contenu du panier"""
    panier = get_panier(request)
    articles = panier.items.all()
    
    context = {
        'panier': panier,
        'articles': articles,
    }
    return render(request, 'cart/panier.html', context)

def modifier_quantite(request, article_id):
    """Modifie la quantité d'un article dans le panier"""
    article = get_object_or_404(ArticlePanier, id=article_id)
    
    if request.method == 'POST':
        quantite = int(request.POST.get('quantite', 1))
        if quantite > 0:
            article.quantite = quantite
            article.save()
        else:
            article.delete()
    
    return redirect('voir_panier')

def supprimer_article(request, article_id):
    """Supprime un article du panier"""
    article = get_object_or_404(ArticlePanier, id=article_id)
    article.delete()
    return redirect('voir_panier')