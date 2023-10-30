from django.contrib import admin
from .models import Loja, Produto, Usuario, ListaDesejos

# Register your models here.

admin.site.register(Loja)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(ListaDesejos)