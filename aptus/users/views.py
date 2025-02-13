from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import Users



# Create your views here.
def home(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('nom')
        password = request.POST.get('password')

        if not email or not password or not first_name:
            messages.error(request,"tous les champs sont requis")

            return render(request, "login.html")
        

        # Vérifiez si l'utilisateur existe
        user = Users.objects.filter(email=email).first()

        if user:
          authenticated_user= authenticate(request,email=email,password=password,first_name=first_name)

          if authenticated_user:
                login(request,authenticated_user)
                messages.success(request,"connexion reussie")
                return redirect('library:start')
          
          else:
                messages.error(request, "mot de passe incorrect ")

                return render(request, 'login.html')
          
        try:
            new_user= Users.objects.create_user(email=email,password=password,first_name=first_name)
            login(request,new_user)
            messages.success(request,"utilisateur crée et connecté avec succes")

            return redirect('library:start')
        
        except Exception as e:
            messages.error(request,f"Erreur: {str(e)}")

            return  render(request, "login.html")
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)

    return redirect ('users:login')

                
"""
        # Si l'utilisateur n'existe pas, créez-le
        if not user:
            # Créer un nouvel utilisateur. Assurez-vous que l'email est unique.
            try:
                user = Users.objects.create_user(email=email, password=password)
                
                messages.success(request, "Votre compte a été créé avec succès.")
            except Exception as e:
                messages.error(request, "Erreur lors de la création du compte : " + str(e))
                return redirect('users:login')  # Rediriger vers la page de connexion

        # Authentifier l'utilisateur
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Si l'utilisateur est authentifié avec succès, connectez-le
            login(request, user)
            return redirect('library:start')  # Redirigez vers la page de bibliothèque ou la page d'accueil

        else:
            # Si l'authentification échoue (mauvais mot de passe), afficher un message d'erreur
            messages.error(request, "Identifiants incorrects. Veuillez réessayer.")
            return redirect('users:login')  # Redirige vers la page de connexion

    return render(request, "login.html")"""

"""def login(request):

    return render(request, "login.html")
"""
"""
def login_view(request):
    if request.method == 'POST':
        email=  request.POST.get('email')
        password = request.POST.get('password')
        user= Users.objects.filter(email=email).first()
        if not user:
            user = Users.objects.create_user( email=email, password=password)
        user = authenticate(request,email=email, password=password)
        if  user is not None:   
            user.save()
            login(request,user)
            return redirect('library:start')
        
    return render(request,"login.html")"""