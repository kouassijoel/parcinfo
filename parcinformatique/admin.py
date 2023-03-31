from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import path
from django.shortcuts import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import *
from .models import *
User = get_user_model()

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    
    
    list_display = ['email', 'nom','prenom','numero_telephone','status','profile','supprimer','detail']
    list_filter = ['status','email']
    fieldsets = (
    (None, {'fields': ('email', 'password',)}),
    ('Personal info', {'fields': ('nom','prenom','numero_telephone','profile',)}),
    ('Permissions', {'fields': ('status',)}),
    )
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('profile','nom','prenom','numero_telephone','email', 'password','password',)}
    ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
    ordering = ['-id']
    filter_horizontal = ()
    
    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
           del actions['delete_selected']
        return actions
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
   
    
@admin.register(Ressource)
class AdminRessource(admin.ModelAdmin):
    list_display = ("id","nom", "prenom","numero_telephone","service",'detail',"supprimer")
    search_fields = ["numero_telephone"]
    ordering = ['-id']
    list_per_page = 10

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['service'].widget.can_change_related = False
        form.base_fields['type_pieces'].widget.can_view_related = False
        form.base_fields['type_pieces'].widget.can_change_related = False
        form.base_fields['service'].widget.can_view_related = False
        return form
    

    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        #view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse('admin:detail', args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    def detail_view(self, request, id_materiel):
      ressource = Ressource.objects.get(pk=id_materiel)
      context ={"ressource": ressource}
      return render(request, 'parcinformatique/detail_ressource.html',context)
       
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='detail'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            #path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls

    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#    materiel = models.ManyToManyField(Materiel)
@admin.register(Materiel)
class AdminMateriel(admin.ModelAdmin):
    list_display =('id',"numero_serie","marque",'modele','etat_achat','fournisseur',"date_acquisition",'detail','supprimer')
    ordering = ['-id']
    search_fields = ["numero_serie"]
    list_per_page = 10
    #change_form_template = 'parcinformatique/parc_change_form.html'

      
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['fournisseur'].widget.can_change_related = False
        form.base_fields['fournisseur'].widget.can_view_related = False
        form.base_fields['type_materiel'].widget.can_change_related = False
        form.base_fields['type_materiel'].widget.can_view_related = False
        return form
    
    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def add_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    

    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        #view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse("admin:detail6", args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    
    def detail_view(self, request, id_materiel):
      materiel = Materiel.objects.get(pk=id_materiel)
      context ={"materiel": materiel}
      return render(request, 'parcinformatique/parc_change_form.html',context)
       
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='detail6'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            #path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls
    #Cette fonction permet de supprimer l'action
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Fournisseur)
class AdminFourisseur(admin.ModelAdmin):
    list_display = ("id","raison_social","email","telephone",'detail',"supprimer")
    search_fields = ["raison_socail"]
    ordering = ['-id']
    list_per_page = 10

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def add_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)

    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        #view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse('admin:detail1', args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    def detail_view(self, request, id_materiel):
      fournisseur = Fournisseur.objects.get(pk=id_materiel)
      context ={"fournisseur": fournisseur}
      return render(request, 'parcinformatique/detai_fournisseur.html',context)
       
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='detail1'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            #path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
#Action pour faire la restitution des des materiels
@admin.register(Attribution)
class AdminAttribution(admin.ModelAdmin):
    list_display = ('id','ressource','mumero_de_serie','date_debut','detail', 'modif','pdf')
    search_fields = ["resource",'mumero']
    ordering = ['-id']
    list_per_page = 10
    #change_form_template = "parcinformatique/base.html"

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def add_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['mumero_de_serie'].widget.can_change_related = False
        form.base_fields['ressource'].widget.can_view_related = False
        form.base_fields['ressource'].widget.can_change_related = False
        form.base_fields['mumero_de_serie'].widget.can_view_related = False
        return form
       
    def detail(self, obj):
         url = reverse('admin:confirm_url',args=[obj.id,])
         html = '<input class="btn btn-primary" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(url)
         return format_html(html)
    
    #Fonction pour la generation d'un fichier PDF
    def render_pdf_view(self,request,id):
        attributition = Attribution.objects.get(pk=id)
        materiel = Materiel.objects.all()
        ressource = Ressource.objects.all()
        user = request.user
        template_path = "parcinformatique/test_pdf.html"
        context = {'materiel': materiel,'attribution': attributition,'ressource': ressource,'user':user}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="ressource.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    
    def modif(self, obj):
        view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Modif" />'.format(link)
        return format_html(html)
    
    def pdf(self, obj):
        url = reverse('admin:pdf-test',args=[obj.id,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Generer PDF" />'.format(url)
        return format_html(html)
    
    def detail_view(self, request, id_materiel):
      attributon = Attribution.objects.get(pk=id_materiel)
      materiel = Materiel.objects.all()
      ressource = Ressource.objects.all()
      context ={"attribution": attributon,"materiel": materiel, 'ressource':ressource}
      return render(request, 'parcinformatique/detail_restitution.html',context)
       
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='confirm_url'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls
    
    

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
@admin.register(Maintenance)
class AdminMaintenance(admin.ModelAdmin):
    list_display = ('id',"materiels","maintenancier",'date_part','date_retour','status','detail',"supprimer")
    search_fields = ["materiel",'maintenacier']
    ordering = ['id']
    list_per_page = 10
    

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['materiels'].widget.can_change_related = False
        form.base_fields['maintenancier'].widget.can_view_related = False
        form.base_fields['maintenancier'].widget.can_change_related = False
        form.base_fields['materiels'].widget.can_view_related = False
        return form
    
    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        #view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse("admin:detail4", args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    
    def detail_view(self, request, id_materiel):
        maintenance = Maintenance.objects.get(pk=id_materiel)
        context ={"maintenance": maintenance}
        return render(request, 'parcinformatique/detail_maintenance.html',context)
       
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='detail4'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            #path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
@admin.register(Maintenancier) 
class AdminMaintenancier(admin.ModelAdmin):
      list_display = ('id','raison_social','email','situation_geographique','telephone','detail','supprimer')
      search_fields = ["raison_socail"]
      list_per_page = 10


      def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
      
      def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
      
      def detail(self, obj):
        #view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse("admin:detail3", args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    
      def detail_view(self, request, id_materiel):
        maintenancier = Maintenancier.objects.get(pk=id_materiel)
        context ={"maintenancier": maintenancier}
        return render(request, 'parcinformatique/detail_maintenancier.html',context)
       
      def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='detail3'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            #path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls
      
        
        
      def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.register(TypeMateriel)
class AdminTypeMateriel(admin.ModelAdmin):
    list_display = ("id","libelle","supprimer","detail")

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
class AdminRestitution(admin.ModelAdmin):

    list_display = ['id','materiel','ressource','date_restitution','detail','supprimer']
    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def add_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save'] = True
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)
    
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['ressource'].widget.can_view_related = False
        form.base_fields['ressource'].widget.can_change_related = False
        return form
    
    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here 
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def add_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_delete'] = False # Here
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_history'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)
    
    
    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(request, obj, **kwargs)
        form.base_fields['ressource'].widget.can_view_related = False
        form.base_fields['ressource'].widget.can_change_related = False
        form.base_fields['materiel'].widget.can_view_related = False
        form.base_fields['materiel'].widget.can_change_related = False
        return form
    
    def supprimer(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk,])
        html = '<input class="btn btn-danger" type="button" onclick="location.href=\'{}\'" value="Supprimer" />'.format(link)
        return format_html(html)
    
    def detail(self, obj):
        #view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse("admin:detail5", args=[obj.pk,])
        html = '<input class="btn btn-info" type="button" onclick="location.href=\'{}\'" value="Detail" />'.format(link)
        return format_html(html)
    
    
    def detail_view(self, request, id_materiel):
        restitution = Restitution.objects.get(pk=id_materiel)
        context ={"restitution": restitution}
        return render(request, 'parcinformatique/detail2_restitution.html',context)
       
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_materiel>', self.detail_view, name='detail5'),
            #path('deny/<int:id>', self.denied_application, name='denied_url'),
            #path('<int:id>/pdf/', self.render_pdf_view, name='pdf-test'),
        ]
        return custom_urls + urls
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
        
class MyAdminSite(admin.AdminSite):
    index_template = "parcinformatique/test.html"
    def index(self, request, extra_context=None):
        extra_context = {}
        extra_context['materiel'] = Materiel.objects.all().count()
        extra_context['attribution'] = Attribution.objects.all().count()
        extra_context['maintenance'] = Maintenance.objects.all().count()
        extra_context['somme'] = Materiel.objects.all().count() - Attribution.objects.all().count()

        return super(MyAdminSite, self).index(request, extra_context)


my_admin_site = MyAdminSite(name='myadmin')
my_admin_site.register(Materiel,AdminMateriel)
my_admin_site.register(Fournisseur,AdminFourisseur)
my_admin_site.register(Attribution,AdminAttribution)
my_admin_site.register(Maintenance,AdminMaintenance)
my_admin_site.register(User,UserAdmin)
my_admin_site.register(Ressource,AdminRessource)
my_admin_site.register(Maintenancier,AdminMaintenancier)
my_admin_site.register(Restitution,AdminRestitution)
my_admin_site.register(Service)
my_admin_site.register(TypePieces)
#Modification du siteAdmin
admin.site.site_header = "PARC INFORMATIQUE"
admin.site.site_title = "PARC INFORMATIQUE"
admin.site.index_title = "PARC INFORMATIQUE"
admin.autodiscover()

