from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'myapp/Inicio.html',{"itens": Product.objects.all()})

def about(request):
    return render(request, 'myapp/about.html')

def shop(request):
    return render(request, 'myapp/shop.html')

def index(request):
    return render(request, 'myapp/index.html',{"itens": Product.objects.all()})

def create(request):
    form = ItensProduct
    if request.method == "POST":
        form = ItensProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "myapp/create.html", {"forms":form})



def edit(request, id):
    item = Product.objects.get(pk=id)
    form = ItensProduct(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item = Product.objects.get(pk=id)
            form = ItensProduct(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    item = Product.objects.get(pk=id)
    return render(request, "myapp/read.html", {"item":item})

def delete(request, id):
    item = Product.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

# def card_create(request):
#     id_user = 1
#     cart = Cart(user=id_user)
#     cart.save()
        
def add_cart(request, id):
    id_user = 1
    cart = Cart(id_user=id_user)
    cart.save()
    cart= Cart.objects.get(user=id_user)
    quantidade = 1
    add = CartItem(product = id, quantity = quantidade, cart = cart.id)
    add.save()
