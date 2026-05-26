from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'preco',
        'quantidade'
    )


admin.site.register(Produto, ProdutoAdmin)