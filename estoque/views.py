from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import F

from .models import Estoque
from .forms import EstoqueForm

def index(request):
    produtos = Estoque.objects.all()
    return render(request, 'estoque/index.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            novo_produto = form.save(commit=False)
            novo_produto.produto = form.data['produto']
            novo_produto.quantidade_em_estoque = form.data['quantidade_em_estoque']
            novo_produto.estoque_minimo = form.data['estoque_minimo']
            novo_produto.save()
            return redirect('index')
    else:
        form = EstoqueForm()        
    return render(request, 'estoque/form_produto.html', {'form': form})


def remover_produto(request, pk):
    produto_para_remover = Estoque.objects.get(pk=pk)
    produto_para_remover.delete()
    messages.success(request, f'O produto {produto_para_remover.produto} foi removido com sucesso!')
    return redirect('index')

def modificar_produto(request, pk):
    produto_para_modificar = Estoque.objects.get(pk=pk)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=produto_para_modificar)
        if form.is_valid():
            produto_para_modificar = form.save(commit=False)
            produto_para_modificar.produto = form.data['produto']
            produto_para_modificar.quantidade_em_estoque = form.data['quantidade_em_estoque']
            produto_para_modificar.estoque_minimo = form.data['estoque_minimo']
            produto_para_modificar.save()
            messages.success(request, f'O produto {produto_para_modificar.produto} foi alterado com sucesso!')
            return redirect('index')
    else:
        form = EstoqueForm(instance=produto_para_modificar)
    return render(request, 'estoque/form_produto.html', {'form': form})


    return redirect('index')


def produtos_em_falta(request):
    todos_produtos = Estoque.objects.all()
    produtos_em_falta = todos_produtos.filter(quantidade_em_estoque__lte = F('estoque_minimo'))
    return render(request, 'estoque/index.html', {'produtos': produtos_em_falta})



# Create your views here.
