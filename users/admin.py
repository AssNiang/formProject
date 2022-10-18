from django.contrib import admin

# Register your models here.
from .models import User, Professeur

admin.site.register(User)


class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email")

admin.site.register(Professeur, ProfesseurAdmin)