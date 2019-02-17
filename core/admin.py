from django.contrib import admin

# Register your models here.
from .models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
admin.site.register(Cadastro, CadastroAdmin)