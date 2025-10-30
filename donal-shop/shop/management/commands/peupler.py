from django.core.management.base import BaseCommand
from shop.models import Categorie, Produit

class Command(BaseCommand):
    help = 'Peuple la base de données avec des données de test'
    
    def handle(self, *args, **options):
        # Créer des catégories
        electronique, created = Categorie.objects.get_or_create(
            nom="Électronique",
            defaults={'description': 'Appareils électroniques et gadgets'}
        )
        
        # Créer des produits
        produits_data = [
            {'nom': 'Sac 8080', 'prix': 3400.00, 'description': 'Sac élégant et pratique'},
            {'nom': 'Médecin n01', 'prix': 20000.00, 'description': 'Appareil médical professionnel'},
            {'nom': 'Volo', 'prix': 20000.00, 'description': 'Appareil électronique Volo'},
            {'nom': 'Volo 8080', 'prix': 2300.00, 'description': 'Nouvelle version Volo 8080'},
        ]
        
        for data in produits_data:
            produit, created = Produit.objects.get_or_create(
                nom=data['nom'],
                defaults={
                    'prix': data['prix'],
                    'description': data['description'],
                    'categorie': electronique,
                    'en_stock': True
                }
            )
            if created:
                self.stdout.write(f"✅ Produit créé: {produit.nom}")
        
        self.stdout.write(
            self.style.SUCCESS('🎉 Base de données peuplée avec succès!')
        )