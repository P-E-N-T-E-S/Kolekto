from django.contrib import admin
from .models import Loja, Produto, Usuario

# Register your models here.

admin.site.register(Loja)
admin.site.register(Produto)
admin.site.register(Usuario)