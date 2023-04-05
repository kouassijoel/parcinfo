from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManger(BaseUserManager):

    def create_user(self,email, password=None):
        """Crée et enregistrer un ulitlisateur avec"""
        if not email:
            raise ValueError("Les utilsateur doit avoir une addresse-email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password):
        """
        Crée et enregistre un utilisateur du staff avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        Crée et enregistre un superutilisateur avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):


   
    objects = UserManger()
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=100)
    profile = models.CharField(max_length=50,default=True ,choices=[ ('IT',('IT')),
                                                      ('SUPERVISEUR', ('SUPERVISEUR'))])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True) # a admin user; non super-user
    status = models.BooleanField(default=False) # a superuser
    # remarquez l'absence du "champ password", c'est intégré pas besoin de preciser.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password sont requis par défaut.

    class Meta:
        verbose_name = "Utilisateur"

    def get_full_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email
    def get_short_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "L'utilisateur a-t-il une autorisation spécifique ?"
        # Réponse la plus simple possible : Oui, toujours
        return True
    def has_module_perms(self, app_label):
        "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"
        # Réponse la plus simple possible : Oui, toujours
        return True
    @property
    def is_staff(self):
        "L'utilisateur est-il un membre du personnel ?"
        return self.staff
    @property
    def is_admin(self):
        "L'utilisateur est-il un membre administrateur?"
        return self.status
    
    def get_all_permissions(user=None):
        if user.is_admin or user.is_staff:
            return set()
      


# Create your models here.

#Creation de la table service"
class Service(models.Model):
    SERVICE = [
        ("NGSER", 'NGSER'),
        ("NOKIA", 'NOKIA'),
        ('GOPA','GOPA'),
        ('HUAWE','HUAWE'),
    ]
    libelle = models.CharField(max_length=20, choices=SERVICE)
    
    def __str__(self):
        return self.libelle


#Creation de la taable Type materiel
class TypeMateriel(models.Model):
    libelle = models.CharField(max_length=50, choices=[('PC',('PC')),('DISQUE DUR',('DISQUE DUR')),('IMPRIM',('IMPRIM'))])

    def __str__(self):
        return self.libelle


class Fournisseur(models.Model):
    raison_social = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    situation_geographique = models.CharField(max_length=50,default=True)
    domaine_activite = models.CharField(max_length=50,blank=True,default=True)

    

    def __str__(self):
        return self.raison_social
#Creation de la table Materiel
class Materiel(models.Model):

    ETAT_ACHAT = [
        ('NEUF', 'NEUF'),
        ('OCCASION', 'OCCASION'),
    ]

    CONSTRUCTEUR = [
        ('HP','HP'),
        ('DELL','DELL'),
        ('LENEVO','LENEVO'),
        ('ASUS','ASUS'),
        ('ACER','ACER'),
        ('MAC','MAC'),
        ('TSHIBA','TASHIBA'),
    ]


    DISQUE_DUR =[
        ('128G','128G'),
        ('250G','250G'),
        ('320G','320G'),

        ('500G','500G'),
        ('750G','750G'),
        ('1TO','1TO'),
    ]

    TYPE_DISQUE_DUR = [
        ('HDD','HDD'),
        ('SSD SATA','SSD SATA'),
        ('SSD M2','SSD M2'),
    ]
    TAILLE_ECRAN = [
        ('10 Pouce','10 Pouce'),
        ('13 Pouce','13 Pouce'),
        ('14 Pouce','14 Pouce'),
        ('15 Pouce','15 Pouce'),
        ('17 Pouce','17 Pouce'),
    ]
    type_materiel = models.ForeignKey(TypeMateriel,on_delete=models.CASCADE)
    marque = models.CharField(max_length=10, choices=CONSTRUCTEUR)  
    numero_serie = models.CharField(max_length=100)
    modele = models.CharField(max_length=50)
    processeur = models.CharField(max_length=10, choices=[('Celeron', ('Celeron')),('Core i3',('Core i3')),('Core i5',('Core i5')),
                                                      ('Core i7', ('Core i7')),('Core i9', ('Core i9'))])
    rame = models.PositiveIntegerField()
    disque_dur = models.CharField(max_length=10, choices=DISQUE_DUR)
    type_disque_dur = models.CharField(max_length=10,choices=TYPE_DISQUE_DUR)
    taille_ecran = models.CharField(max_length=50, choices=TAILLE_ECRAN)
    etat_achat = models.CharField(max_length=20,choices=ETAT_ACHAT)
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE,default=True)
    garantie = models.PositiveIntegerField(help_text="CE CHAMP EST EN MOIS")  
    date_acquisition = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return self.numero_serie
    
class TypePieces(models.Model):
    libelle = models.   CharField(max_length=50, choices=[('CNI', ('CNI')),('PASSPORT',('PASSPORT')),('PERMIS CONDUITE',('PERMIS CONDUITE')),
                                                      ('ATTESTATION', ('ATTESTATION'))])
    
    
    def __str__(self):
        return self.libelle
    
#Creation de la table  ressource dans la base de donné"
class Ressource(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    service =models.ForeignKey(Service, on_delete=models.PROTECT)
    date_naissances = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    fonction = models.CharField(max_length=50, default=True)
    type_pieces = models.ForeignKey(TypePieces,on_delete=models.CASCADE)
    numero_pieces = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    numero_telephone = models.CharField(max_length=10)
   
    def __str__(self):
        return str(self.nom) + ' ' +  str(self.prenom)
    

class Maintenancier(models.Model):
    raison_social = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    situation_geographique = models.CharField(max_length=50,default=True)
    domaine_activite = models.CharField(max_length=50,blank=True,default=True)



    def __str__(self):
        return self.raison_social
    
    #Creation de la table type de piece

#Creation de la table Attribution
class Attribution(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    mumero_de_serie = models.OneToOneField(Materiel, on_delete=models.CASCADE,unique=True)
    date_debut = models.DateField("Debut d'attribution", auto_now_add= True)

    def __str__(self):
        return str(self.date_debut)


class Maintenance(models.Model):
    materiels = models.ForeignKey(Materiel, on_delete =models.CASCADE)
    maintenancier = models.ForeignKey(Maintenancier, on_delete = models.CASCADE)
    date_part = models.DateField(help_text="Date de part" ,blank=True,null=True)
    date_retour = models.DateField(help_text="Date de retour" ,blank=True,null=True)
    status = models.CharField(max_length=50, choices=[('EN MAINTENANCE', ('En maintenance')),
                                                      ('EN STOCK', ('En stock'))], default=True)


    def __str__(self):
        return str(self.date_part)


class Restitution(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, default= True)
    description = models.TextField(max_length=150)
    date_restitution = models.DateField(auto_now_add=True)
    fichier = models.FileField(upload_to="upload", max_length=254)
 
    @property
    def ressource_restitution(self):
        for materiel in self.ressource_restitution.all():
            return materiel

    def __str__(self):
        return self.description
   