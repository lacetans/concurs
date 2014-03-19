from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
import os

# Create your models here.

def filebuilder(instance,filename):
    ext = filename.split(".")[-1]
    name = os.urandom(16).encode("hex")
    folder = "uploads/" + instance.__class__.__name__ + "/"
    return folder + str(name) + "." + str(ext)
    
class Enviament(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.DecimalField(max_digits=9,decimal_places=0)
    data = models.DateTimeField("data de carrega")
    titol = models.CharField(max_length=100)
    arxiu = models.FileField(upload_to=filebuilder)
    def __unicode__(self):
        return os.path.basename(self.arxiu.name)

@receiver(post_delete, sender=Enviament)
def enviament_esborra_arxiu(sender, instance, **kwargs):
    #if instance.arxiu.isfile(instance.file.path):
    #    os.remove(instance.arxiu.path)
    instance.arxiu.delete(False)

class Cartell(Enviament):
    pass

class Narracio(Enviament):
    pass

class Poesia(Enviament):
    pass
    
class Assaig(Enviament):
    pass

# configuracio de la site (singleton)
class Config(models.Model):
    activa = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Config, self).save(*args, **kwargs)
        
    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
