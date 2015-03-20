# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django.core.mail import EmailMessage

from datetime import datetime

from cartells.models import *

# opcions pel menu
opcions = ( Cartell.__name__, Narracio.__name__, Poesia.__name__, Assaig.__name__ )

class EnviamentForm(ModelForm):
    class Meta:
        model = Enviament
        fields = ['nom','email','telefon','titol','arxiu']
    # TODO: captcha

def index(request):
    conf = Config()
    # TODO: tancar terminis
    #if conf.activa.

    # opcio (Cartell,Narracio,...) per defecte
    opcio = Cartell.__name__
    # mirem opcio triada
    op = request.GET.get("opcio")
    if op:
        opcio = op
    print opcio
    
    if request.method=="POST":
        if opcio == Cartell.__name__:
            instancia = Cartell()
        elif opcio == Narracio.__name__:
            instancia = Narracio()
        elif opcio == Poesia.__name__:
            instancia = Poesia()
        elif opcio == Assaig.__name__:
            instancia = Assaig()
        else:
            return HttpResponse("Error en l'aplicacio: opcio invalida")

        form = EnviamentForm(request.POST, request.FILES, instance=instancia )
        if form.is_valid():
            # comprovar que l'email no esta repetit
            # AL FINAL NO HO COMPROVEM
            """email = form.cleaned_data["email"]
            try:
                if opcio==Cartell.__name__:
                    c2 = Cartell.objects.get(email=email)
                elif opcio==Narracio.__name__:
                    c2 = Narracio.objects.get(email=email)
                elif opcio==Poesia.__name__:
                    c2 = Poesia.objects.get(email=email)
                elif opcio==Assaig.__name__:
                    c2 = Assaig.objects.get(email=email)
                else:
                    return HttpResponse("Error en l'aplicacio: opcio invalida (2)")
            except:"""
            # email no existeix: entrar-ho a la BBDD
            instancia.data = datetime.now()
            enviament = form.save()
            subject = "Concurs Lacetània Sant Jordi"
            body = """
Benvolguda/ut,

has efectuat una tramesa per participar al concurs Lacetània de Sant Jordi.
Merci per particpar! :)

Categoria: %s
Codi: %s

Aquest codi només és per si vols fer alguna comprovació o reclamació al jurat.

Sort!

Informàtica Lacetània (infla.cat)
""" % ( opcio, enviament.arxiu )
            email = EmailMessage( subject, body, from_email='noreply@infla.cat', to=[enviament.email] )
            email.send(fail_silently=False)

            missatge = """
Enviat! :)<br>
Merci per la teva participació!<br><br>
Rebràs un email amb les dades de la teva candidatura. Sort!
"""
            return HttpResponse( missatge )

    else:
        form = EnviamentForm()
        
    return render(request,"cartells/form.html", {"form":form, "opcio":opcio, "opcions":opcions} )
