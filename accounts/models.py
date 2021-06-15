from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone

class Employé(models.Model):
    session_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    telephone = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    adresse = models.CharField(max_length=200, null=True)
    titre = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.nom, self.prenom)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Employé.objects.create(user=instance)


class Projet(models.Model):
    ETAT = (
        ('Terminé', 'Terminé'),
        ('En cours', 'En cours'),
        ('Suspendu', 'Suspendu'),
    )
    designation = models.CharField(max_length=200, null=True)
    responsable = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    durée_en_semaines = models.PositiveIntegerField(null=True)
    statut = models.CharField(max_length=200, null=True, choices=ETAT)

    def __str__(self):
        return self.designation

class Fabricant(models.Model):
    nom = models.CharField(max_length=200, null=True)
    reference = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Piece(models.Model):
    CATEGORY = (
        ('Electrique', 'Electrique'),
        ('Mecanique', 'Mecanique'),
    )
    designation = models.CharField(max_length=200, null=True)
    reference = models.CharField(max_length=200, null=True)
    categorie = models.CharField(max_length=200, null=True, choices=CATEGORY)
    prix = models.FloatField(default=0.0, null=True)
    fabricant = models.ForeignKey(Fabricant, null=True, on_delete= models.SET_NULL) 
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.designation

class Fournisseur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    reference = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    '''email = models.EmailField(max_length=100, null=True)
    adresse = models.CharField(max_length=200, null=True)
    pieces = models.ForeignKey(Piece, null=True, on_delete= models.SET_NULL)''' 
    def __str__(self):
        return self.nom


class Customer(models.Model):
    nom = models.CharField(max_length=200, null=True)
    po = models.CharField(max_length=200, null=True) 

    def __str__(self):
        return self.nom

class POCustomer(models.Model):
    num = models.CharField(max_length=200, null=True) 
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.num

class Demande(models.Model):
    ETAT = (
        ('Validée', 'Validée'),
        ('Non Validée', 'Non Validée'),
    )

    DEVISE = (
        ('TND','TND'),
        ('€','€'),
        ('$','$'),
    )

    REQTYPE = (
        ('Besoin Projet' , 'Besoin Projet'),
        ('Frais géneraux (SAMM)','Frais géneraux (SAMM)'),
        ('Immobilisation (SAMM)','Immobilisation (SAMM)')
    )
    #Num_RFQ = models.IntegerField(null=True)
    Project_Ref = models.ForeignKey(Projet, null=True, on_delete= models.SET_NULL)  
    Application_Date = models.DateTimeField(auto_now_add=True, null=True)
    Customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) 
    PO_Customer = models.ForeignKey(POCustomer, null=True, on_delete= models.SET_NULL) 
    Requester = models.CharField(max_length=200, null=True) 
    Request_Type = models.CharField(max_length=200, null=True, choices=REQTYPE)
    Speciality = models.CharField(max_length=200, null=True)
    Desired_Delivery_Date = models.CharField(max_length=200, null=True)
    Supplier_1 = models.ForeignKey(Fournisseur, null=True, on_delete= models.SET_NULL, related_name='supp1')
    Supplier_2 = models.ForeignKey(Fournisseur, null=True, on_delete= models.SET_NULL, related_name='supp2')
    Supplier_3 = models.ForeignKey(Fournisseur, null=True, on_delete= models.SET_NULL, related_name='supp3')
    Delay_1 = models.IntegerField(null=True)
    Delay_2 = models.IntegerField(null=True)
    Delay_3 = models.IntegerField(null=True)
    Quotation_Number_1 = models.CharField(max_length=200,null=True)
    Quotation_Number_2 = models.CharField(max_length=200,null=True)
    Quotation_Number_3 = models.CharField(max_length=200,null=True)
    Initial_Cost_Cotation_1 = models.IntegerField(null=True)
    Initial_Cost_Cotation_2 = models.IntegerField(null=True)
    Initial_Cost_Cotation_3 = models.IntegerField(null=True)
    Devise_1 = models.CharField(max_length=200, null=True, choices=DEVISE)
    Devise_2 = models.CharField(max_length=200, null=True, choices=DEVISE)
    Devise_3 = models.CharField(max_length=200, null=True, choices=DEVISE)
    File_1 = models.FileField(upload_to=None, null=True, blank="true")   
    File_2 = models.FileField(upload_to=None, null=True, blank="true")   
    File_3 = models.FileField(upload_to=None, null=True, blank="true")   
    statut = models.CharField(max_length=200, null=True, choices=ETAT, blank=True)

    def __str__(self):
        return f"Request N°{self.id}"

   
class Demande_Validée(models.Model):
    demande = models.OneToOneField(Demande, null=True, on_delete= models.CASCADE)  
    valid = models.BooleanField(default=False)
    date_validation =  models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"V_Request N°{self.demande.id}"


class Commande(models.Model):
    ETAT = (
        ('Livrée', 'Livrée'),
        ('En cours', 'En cours'),
        ('En retard', 'En retard'),
        ('Annulée', 'Annulée'),
    )
    Request = models.OneToOneField(Demande_Validée, null=True, on_delete=models.CASCADE)
    Final_Cost = models.IntegerField(default=0, null=True)
    Estimated_Delivery_Date = models.CharField(max_length=200, null=True)
    PO_Number = models.IntegerField(default=0, null=True)
    PO_Date = models.CharField(max_length=200, null=True)
    Delivery_Date = models.CharField(max_length=200, null=True)
    date_commande = models.DateTimeField(auto_now_add=True, null=True)

class Csv(models.Model):
    file_name = models.FileField(upload_to='accounts')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
