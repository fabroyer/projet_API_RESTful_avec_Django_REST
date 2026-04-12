from rest_framework.permissions import BasePermission, SAFE_METHODS


# Ici on fait encore quelque chose qui est juste une personnalisation de l'application.
# Cette fonction has_object a déjà un objet, donc SAFE_METHODS déjà prévu par djangorest
# ne peut pas faire de POST contrairement à la même pour un nouvel objet.
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj == request.user
