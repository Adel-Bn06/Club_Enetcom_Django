from django.shortcuts import *
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.http import *
from .models import *
from .forms import *
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views import View

# Create your views here.

#@permission_required('app_enetcom.can_add_membre', raise_exception=True)
def add_membre(request):
    if request.method=='POST':
        form=add_member_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email'] #username-->email
            email=form.cleaned_data['email']
            password = form.cleaned_data['password']
            exist_user=User.objects.filter(email=email)
            if len(exist_user)<1:
                user=User.objects.create_user(username,email,password) # bch tlwjli est ce que fama l user hetha wala
                user.first_name=form.cleaned_data['first_name']
                user.last_name=form.cleaned_data['last_name']
                user.save()
                etudiant=Etudianti()
                etudiant.user=user
                etudiant.first_name = form.cleaned_data.get('first_name')
                etudiant.last_name = form.cleaned_data.get('last_name')
                etudiant.email = form.cleaned_data.get('email')
                etudiant.Numero= form.cleaned_data.get('Numero')
                etudiant.save()
            else:
                etudiant=exist_user[0].etudianti
                membre_club=MembreClubi()
                membre_club.club= request.user.presidentclubi.Club
                membre_club.etud= etudiant
                membre_club.save()
            return redirect('confirme')  
    else:
        form = add_member_form()
     
        return render(request, 'add_membre.html', {'form': form})

def confirmation(request):
    return HttpResponse("votre ajout est bien passé")

def add_pres(request):
    if request.method=='POST':
        form=add_pres_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            club_name = form.cleaned_data['club_name']
            password = form.cleaned_data['password']
            user=User.objects.create_user(username,email,password)
            
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            club, created = Clubi.objects.get_or_create(nom=club_name)
            user.save()
            
            president = Etudianti()
            president.user = user
            president.first_name = form.cleaned_data['first_name']
            president.last_name = form.cleaned_data['last_name']
            president.email = form.cleaned_data['email']
            president.Numero = form.cleaned_data['Numero']
            president.save()

            etudiant=PresidentClubi()
            etudiant.Club=club
            etudiant.user=user
            etudiant.etudi=president
            etudiant.first_name = form.cleaned_data.get('first_name')
            etudiant.last_name= form.cleaned_data.get('last_name')
            etudiant.email = form.cleaned_data.get('email')
            etudiant.Numero= form.cleaned_data.get('Numero')
            etudiant.save()

            membre_club=MembreClubi()
            membre_club.club= club
            membre_club.etud= etudiant
            membre_club.save()

            return redirect('success')  
    else:
        form = add_pres_form()

        return render(request, 'add_pres.html', {'form': form})

def success(request):
    return HttpResponse("votre ajout est bien passé")

def base(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Check if the 'presidentclubi' attribute exists for the user
                if hasattr(user, 'presidentclubi') and user.presidentclubi:
                    return redirect('compte2', id=user.presidentclubi.Club.id)  # Redirige vers compte2 avec l'ID de l'utilisateur
                else:
                    return redirect('hello_user')  # Redirige vers hello_user pour les utilisateurs non-présidents
    else:
        form = LoginForm()
    return render(request, 'base.html', {'form': form})

def compte(request):
    return HttpResponse("Bienvenu dans votre compte")
@login_required(login_url='../base/')
def compte2(request, id):
    membre_clubs = list(MembreClubi.objects.filter(etud=request.user.etudianti).values_list('club',flat=True)) #les identifiants
    clubs= Clubi.objects.filter(id__in=membre_clubs) 
    club=Clubi.objects.get(id=id)
    if request.method == 'POST': 
        form = ActualiteForm(request.POST)
        if form.is_valid():
            act=form.save(commit=False)
            act.club= request.user.presidentclubi.Club
            act.save()
            return redirect('compte2',id=id)  # Rediriger vers la même page après l'ajout d'une actualité
    else:
        form = ActualiteForm()
    actu = actualite.objects.filter(club__id=id)  # Récupérer les actualités du club
    
    return render(request, 'compte2.html', {'form': form, 'act': actu})


#def actualite(request):
  #  return render(request,'Actualites.html')

def chatbox(request):
    return render(request,'Chatbox.html')

def Formations(request):
    return render(request,'Formations.html')

def souvenirs(request):
    return render(request,'souvenirs.html')

def profile(request):
    return render(request,'profile.html')

def parametre(request):
    return render(request,'parametre.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('base'))

from .forms import MessagesForm

class ChatboxView(View):
    template_name = 'chatbox.html'

    def get(self, request, *args, **kwargs):
        form = MessagesForm()
        
        messages = Messages.objects.order_by('timestamp')

        return render(request, self.template_name, {'form': form, 'messages': messages})

    def post(self, request, *args, **kwargs):
         form = MessagesForm(request.POST)
         if form.is_valid():
            recipient_nom = form.cleaned_data['recipient']
        # Recherchez un objet Clubi en fonction du nom du club
            recipient = Clubi.objects.get(nom=recipient_nom)
            message_content = form.cleaned_data['message']
            Messages.objects.create(sender=request.user, recipient=recipient, content=message_content)
            form = MessagesForm()

            return redirect(request.path_info)

    
def welcome_user(request,id=None):
    membre_clubs = list(MembreClubi.objects.filter(etud=request.user.etudianti).values_list('club',flat=True)) #les identifiants
    clubs= Clubi.objects.filter(id__in=membre_clubs) # les informations du club
    dictio = {'user_clubs': clubs}
    if id:
        club=Clubi.objects.get(id=id)
        act=actualite.objects.filter(club__id=id).order_by('date')
        dictio['act']=act
        dictio['club']=club
        return redirect('compte2',id=id)
    return render(request, 'welcome_user.html', dictio)








   


