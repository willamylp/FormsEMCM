from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Preceptores, Graduacao, Residencia, Mestrado, Doutorado, Vinculo_Profissional, Horarios
#, Vinculo_Profissional

admin.site.register(Preceptores)
admin.site.register(Graduacao)
admin.site.register(Residencia)
admin.site.register(Mestrado)
admin.site.register(Doutorado)
admin.site.register(Vinculo_Profissional)
admin.site.register(Horarios)