from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Loja)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(ListaDesejos)
admin.site.register(Denuncia)
admin.site.register(Compra)
admin.site.register(Avaliacao)