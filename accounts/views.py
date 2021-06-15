from django.db.models import query
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Demande, Projet, Piece, Fournisseur, Employé, Commande, Piece, Demande_Validée, Customer, POCustomer
from .forms import DemandeForm, FournisseurForm, CreateUserForm, EmployéForm, CommandeForm, PieceForm, DemandeValForm, CsvModelForm
from .filters import DemandeFilter
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
import csv, io
import pandas as pd

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username ou Password est invalide')

    context = {}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='loginPage')
def home(request):
    demandes = Demande.objects.all().order_by('-Application_Date')
    projets = Projet.objects.all().order_by('-date_creation')
    fournisseurs = Fournisseur.objects.all().order_by('-date_creation')
    total_demandes = demandes.count()
    demandes_validees = Demande_Validée.objects.all().order_by('-date_validation')
    total_demval = demandes_validees.count()
    non_validees = demandes.filter(statut='Non Validée').count()
    context = {'demandes':demandes, 'projets':projets, 'fournisseurs': fournisseurs, 'total_demandes':total_demandes, 'total_demval':total_demval, 'non_validees':non_validees}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier','admin'])
def pieces(request):
    pieces = Piece.objects.all().order_by('-date_creation')
    return render(request, 'accounts/pieces.html', {'pieces': pieces})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier','admin'])
def ajouter_piece(request):
    form = PieceForm()
    if request.method == 'POST':
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'pièce ajoutée avec succès')
            return redirect('/ajouter_piece/')
    context = {'form': form}
    return render(request, 'accounts/pieceform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier','admin'])
def modifier_piece(request, piece_id):
    piece = Piece.objects.get(id=piece_id)
    form = PieceForm(instance=piece)
    if request.method == 'POST':
        form = PieceForm(request.POST, instance=piece)
        if form.is_valid():
            form.save()
            return redirect('/pieces/')   
    context = {'form': form}
    return render(request, 'accounts/pieceform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['magasinier','admin'])
def supprimer_piece(request, piece_id):
    piece = Piece.objects.get(id=piece_id)
    if request.method == 'POST':
        piece.delete()
        return redirect('/pieces/')  
    context = {'item': piece }
    return render(request, 'accounts/deletepiece.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def employés(request):
    employés = Employé.objects.all().order_by('-date_creation')
    return render(request, 'accounts/employés.html', {'employés': employés})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def creer_compte(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'session ajoutée avec succès')
            return redirect('creer_compte')
    context = {'form': form}
    return render(request, 'accounts/session.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def creer_employé(request):
    form = EmployéForm()
    if request.method == 'POST':
        form = EmployéForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'employé ajouté avec succès')
            return redirect('creer_employé')
    context = {'form': form}
    return render(request, 'accounts/employéform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def modifier_employé(request, employé_id):
    employé = Employé.objects.get(id=employé_id)
    form = EmployéForm(instance=employé)
    if request.method == 'POST':
        form = EmployéForm(request.POST, instance=employé)
        if form.is_valid():
            form.save()
            return redirect('/employés/')   
    context = {'form': form}
    return render(request, 'accounts/employéform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def supprimer_employé(request, employé_id):
    employé = Employé.objects.get(id=employé_id)
    if request.method == 'POST':
        employé.delete()
        return redirect('/employés/')  
    context = {'item': employé }
    return render(request, 'accounts/deleteemp.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    demandes = fournisseur.demande_set.all().order_by('-Application_Date')
    total_demandes = demandes.count()
    
    
    '''if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        
        send_mail(
            message_name, # subject
            message,
            message_email, # from email
            [wessimzeckri1999@gmail.com], # to email
        )'''

    return render(request, 'accounts/fournisseur.html', {'fournisseur':fournisseur, 'demandes': demandes, 'total_demandes':total_demandes})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat','admin'])
def fournisseurs(request):
    fournisseurs = Fournisseur.objects.all().order_by('-date_creation')
    return render(request, 'accounts/fournisseurs.html', {'fournisseurs': fournisseurs})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat','admin'])
def creer_fournisseur(request):
    form = FournisseurForm()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fournisseurs/')
    context = {'form': form}
    return render(request, 'accounts/fournisseurform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat','admin'])
def modifier_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    form = FournisseurForm(instance=fournisseur)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('/fournisseurs/')   
    context = {'form': form}
    return render(request, 'accounts/fournisseurform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat','admin'])
def supprimer_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('/fournisseurs/')  
    context = {'item': fournisseur }
    return render(request, 'accounts/deletefourn.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat','admin','chef projet','direction'])
def demval(request):
    demandes_validees = Demande_Validée.objects.all()
    return render(request, 'accounts/demval.html', {'demandes_validees': demandes_validees})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat'])
def lancer_commande(request):
    
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'commande ajoutée avec succès')
            return redirect('/lancer_commande/')
    context = {'form': form}
    return render(request, 'accounts/commandeform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['direction','responsable achat'])
def valider_demande(request, demande_id):


    demand = Demande.objects.get(id=demande_id)
    demandeVal = Demande_Validée.objects.create(demande = demand, valid=True)
    return render(request, 'accounts/success.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['direction','responsable achat'])
def refuser_demande(request, demande_id):
    demand = Demande.objects.get(id=demande_id)
    demand.delete()
    return render(request, 'accounts/dashboard.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['responsable achat', 'admin'])
def commandes(request):
    commandes = Commande.objects.all().order_by('-date_commande')
    return render(request, 'accounts/commandes.html', {'commandes' : commandes})

@login_required(login_url='loginPage')
def projet(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    demandes = projet.demande_set.all().order_by('-date_creation')
    total_demandes = demandes.count()
    return render(request, 'accounts/projet.html', {'projet':projet, 'demandes': demandes, 'total_demandes':total_demandes})

@login_required(login_url='loginPage')
def projets(request):
    projets = Projet.objects.all().order_by('-date_creation')
    return render(request, 'accounts/projets.html', {'projets': projets})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet','admin','responsable achat','direction'])
def demandes(request):
    demandes = Demande.objects.all().order_by('-Application_Date')
    myFilter = DemandeFilter(request.GET, queryset=demandes)
    demandes = myFilter.qs    

    return render(request, 'accounts/demandes.html', {'demandes':demandes, 'myFilter':myFilter})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['direction','responsable achat'])
def demdir(request):
    demandes = Demande.objects.all().order_by('-Application_Date')
    demandesval = Demande_Validée.objects.all().order_by('-date_validation')
    myFilter = DemandeFilter(request.GET, queryset=demandes)
    demandes = myFilter.qs
    '''demandes_validees = demandes.filter(statut='Validée')
    non_validees = demandes.filter(statut='Non Validée')'''
    return render(request, 'accounts/demdir.html', {'demandes':demandes, 'demandesval':demandesval, 'myFilter':myFilter})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['direction'])
def success(request):
    return render(request, 'accounts/success.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet','admin','responsable achat','direction'])
def creer_demande(request):
    form = DemandeForm()
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'demande ajoutée avec succès')           
            return redirect('/creer_demande/')
    context = {'form': form}
    return render(request, 'accounts/demandeform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet','admin'])
def modifier_demande(request, demande_id):
    demande = Demande.objects.get(id=demande_id)
    form = DemandeForm(instance=demande)
    if request.method == 'POST':
        form = DemandeForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('demandes')   
    context = {'form': form}
    return render(request, 'accounts/demandeform.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['chef projet','admin'])
def supprimer_demande(request, demande_id):
    demande = Demande.objects.get(id=demande_id)
    if request.method == 'POST':
        demande.delete()
        return redirect('/')  
    context = {'item': demande }
    return render(request, 'accounts/delete.html', context)



def export(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    demandes = fournisseur.demande_set.all().order_by('-Application_Date')
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Num_RFQ','Project_Ref','Application_Date','Customer','PO_Customer','Requester','Speciality','Desired_Delivery_Date','Quotation_Number','Initial_Cost_Cotation','Devise','Initial_Delivery_Date'])

    for demande in demandes.values_list('Num_RFQ','Project_Ref','Application_Date', 'Customer','PO_Customer','Requester','Speciality','Desired_Delivery_Date','Quotation_Number','Initial_Cost_Cotation','Devise','Initial_Delivery_Date'):
        writer.writerow(demande)
    response['Content-Disposition'] = 'attachment; filename = "demandes.csv" '
    return response

def base(request):
    qs = Fournisseur.objects.all().values( )
    data = pd.DataFrame(qs)
    print(data)
    context = {
        'df' : data
    }
    return render(request, 'accounts/base.html', context )


def upload_file_view(request):
    prompt = {
            'order': 'Order of the CSV should be nom, reference, telephone'
        }
    if request.method == 'GET' :
        return render(request, 'accounts/upload.html', prompt)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Fournisseur.objects.update_or_create(
            nom=column[0],
            reference=column[1],
            telephone=column[2],
        )
    messages.success(request, 'Liste des fournisseurs ajoutée avec succès')
    context = {}
    return render(request, 'accounts/upload.html', context)

def upload_file_customer(request):
    prompt = {
            'order': 'Order of the CSV should be nom, reference, telephone'
        }
    if request.method == 'GET' :
        return render(request, 'accounts/upload.html', prompt)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = Customer.objects.update_or_create(
            nom=column[0],
        )
    messages.success(request, 'Liste des clients ajoutée avec succès')
    context = {}
    return render(request, 'accounts/uploadc.html', context)

def upload_file_customer(request):
    prompt = {
            'order': 'Order of the CSV should be nom, reference, telephone'
        }
    if request.method == 'GET' :
        return render(request, 'accounts/uploadc.html', prompt)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = Customer.objects.update_or_create(
            nom=column[0],
        )
    messages.success(request, 'Liste des clients ajoutée avec succès')
    context = {}
    return render(request, 'accounts/uploadc.html', context)

def upload_file_pocustomer(request):
    prompt = {
            'order': 'Order of the CSV should be nom, reference, telephone'
        }
    if request.method == 'GET' :
        return render(request, 'accounts/uploadpoc.html', prompt)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = POCustomer.objects.update_or_create(
            
            num = column[1],
        )
    messages.success(request, 'Liste des BC clients ajoutée avec succès')
    context = {}
    return render(request, 'accounts/uploadpoc.html', context)

def mail(request):
    if request.method == 'POST' : 
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        
        send_mail(
            message_name, # subject
            message,
            message_email, # from email
            [wessimzeckri1999@gmail.com], # to email
        )

        return render(request, 'accounts/contact.html', {'message_name':message_name , 'message_email' :message_name , 'message' : message}) 

    else:
        return render(request, 'accounts/contact.html', {})