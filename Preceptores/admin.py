from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Preceptores, Graduacao, Residencia, Mestrado, Doutorado, Vinculo_Profissional

admin.site.register(Preceptores)