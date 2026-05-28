from django.shortcuts import render, redirect
from .models import Produto

def inicio(request):

    if request.method == 'POST':

        produto_id = request.POST.get('produto_id')
        acao = request.POST.get('acao')

        produto = Produto.objects.get(id=produto_id)

        # DIMINUI ESTOQUE
        if acao == 'vender':

            if produto.quantidade > 0:
                produto.quantidade -= 1

        # AUMENTA ESTOQUE
        elif acao == 'adicionar':

            produto.quantidade += 1

        produto.save()

        return redirect('/')

    produtos = Produto.objects.all()

    return render(request, 'inicio.html', {'produtos': produtos})
    
    From django,shortcuts import render, redirect, get object_er_404
Fron models import Produto
pef vender_produto (request, produto_id) :
Produto - get_object_or_404(Produto, 1d-produto_id)
produto quantidade t= 1
produto. save ()
return redirect ("inicio:)