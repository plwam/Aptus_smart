# backends.py

from django.contrib.auth.backends import ModelBackend
from .models import Users

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # On cherche l'utilisateur avec l'email (username est en fait l'email ici)
            user = Users.objects.get(email=username)
            if user.check_password(password):  # Vérifie si le mot de passe est correct
                return user
        except Users.DoesNotExist:
            return None  # Si l'utilisateur n'existe pas, retourner None
