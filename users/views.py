from django.shortcuts import render
from django.http import HttpResponse
from users.forms import ProfesseurForm
from .models import Professeur

# Create your views here.
def view_form(request, num_form=""):
    if num_form == "formprof":
        formulaire = "form1"

        fm = ProfesseurForm(request.POST)
        errors = not fm.is_valid()

        if not errors:
            fm.save()
            
            return HttpResponse("<h1>Données enrgistrées avec succès</h1>")

        form = ProfesseurForm
        context={"formulaire":formulaire, "form": form, "errors": errors}

        return render(request, "users/index.html", context)

    elif num_form == 'formprof2':
        formulaire = "form2"
        try:
            result = dict(request.POST)
        
            teacher = Professeur(
                prenom=result["fname"][0],
                nom=result["lname"][0],
                email=result["email"][0],
                contact_prof=result["phone"][0],
                date_d_adhesion=result["date"][0],
                chef_departement= True if result["chef"][0]=='on' else False
                )

            teacher.save()
            return HttpResponse("<h1>Données enrgistrées avec succès</h1>")

        except:
            context = {"formulaire":formulaire, "result": result, "errors":True}
            return render(request, "users/index.html", context)
    else:
        return HttpResponse("<h1>Le formulaire n'existe pas</h1>")

    