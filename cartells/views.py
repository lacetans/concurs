from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm

from datetime import datetime

from cartells.models import *

# opcions pel menu
opcions = ( Cartell.__name__, Narracio.__name__, Poesia.__name__, Assaig.__name__ )

class CartellForm(ModelForm):
    class Meta:
        model = Cartell
        fields = ['nom','email','telefon','titol','arxiu']
    # TODO: captcha

class NarracioForm(ModelForm):
    class Meta:
        model = Narracio
        fields = ['nom','email','telefon','titol','arxiu']
    # TODO: captcha

class PoesiaForm(ModelForm):
    class Meta:
        model = Poesia
        fields = ['nom','email','telefon','titol','arxiu']
    # TODO: captcha

class AssaigForm(ModelForm):
    class Meta:
        model = Assaig
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
        if opcio==Cartell.__name__:
            instancia = Cartell()
            form = CartellForm(request.POST, request.FILES, instance=instancia )
        elif opcio==Narracio.__name__:
            instancia = Narracio()
            form = NarracioForm(request.POST, request.FILES, instance=instancia )
        elif opcio==Poesia.__name__:
            instancia = Poesia()
            form = PoesiaForm(request.POST, request.FILES, instance=instancia )
        elif opcio==Assaig.__name__:
            instancia = Assaig()
            form = AssaigForm(request.POST, request.FILES, instance=instancia )
        else:
            return HttpResponse("Error en l'aplicacio: opcio invalida")

        if form.is_valid():
            # comprovar que l'email no esta repetit
            email = form.cleaned_data["email"]
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
            except:
                # email no existeix: entrar-ho a la BBDD
                instancia.data = datetime.now()
                form.save()
                return HttpResponse("Enviat! :)")
            # email existent a la BBDD
            # TODO: enviar email notificacio
            return HttpResponse("Ja has enviat un document amb aquest email en aquesta categoria.")

    else:
        if opcio==Cartell.__name__:
            form = CartellForm()
        elif opcio==Narracio.__name__:
            form = NarracioForm()
        elif opcio==Poesia.__name__:
            form = PoesiaForm()
        elif opcio==Assaig.__name__:
            form = AssaigForm()
        else:
            return HttpResponse("Error en l'aplicacio: opcio invalida (3)")
        
    return render(request,"cartells/form.html", {"form":form, "opcio":opcio, "opcions":opcions} )
