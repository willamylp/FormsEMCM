from django.urls import path
from .views import RegistroPreceptor, ListarPreceptores

urlpatterns = [
    path("RegistrarPreceptor/", RegistroPreceptor, name="RegistroPreceptor"),
    path("ListarPreceptores/", ListarPreceptores, name="ListarPreceptores"),
    #path("AtualizarHost/<int:id>/", AtualizarHost, name="AtualizarHost"),
    #path("DeletarHost/<int:id>/", DeletarHost, name="DeletarHost"),
]