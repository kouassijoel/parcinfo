from django.urls import path
from parcinformatique.views import *

app_name = "parcinformatique"

urlpatterns = [
    path('', restitution_form, name='restitution'),
]