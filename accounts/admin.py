from django.contrib import admin

from .models import Projet, Piece, Demande, Fournisseur, Fabricant, Employé, Commande, Demande_Validée, Customer, POCustomer, Csv

admin.site.register(Projet)
admin.site.register(Piece)
admin.site.register(Demande)
admin.site.register(Demande_Validée)
admin.site.register(Fournisseur)
admin.site.register(Fabricant)
admin.site.register(Employé)
admin.site.register(Commande)
admin.site.register(Customer)
admin.site.register(POCustomer)
admin.site.register(Csv)
#admin.site.register(Tag)