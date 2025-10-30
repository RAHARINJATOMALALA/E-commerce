from .views import get_panier

def cart(request):
    if request.path.startswith('/admin/'):
        return {}
    
    panier = get_panier(request)
    return {
        'panier': panier
    }