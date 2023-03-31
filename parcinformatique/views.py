from django.shortcuts import render, redirect
from . forms import AttributionsForm
from .models import *
from django.views.generic.detail import DetailView

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from parcinformatique.utils import render_to_pdf #created in step 4
# Create your views here.

def restitution(request):
    materiel = Materiel.objects.all().count()
    context = {"materiel": materiel}
    return render(request,'parcinformatique/test.html',context)

def restitution_form(request):  
    form = AttributionsForm()
    
    return render(request, 'parcinformatique/restitution.html', {'form': form})


