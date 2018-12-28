from django.shortcuts import render, redirect
from .models import Item
import datetime

def updateCartItem(item, quantity):
    item['quantity'] = quantity
    item['sum'] = float(item['price']) * quantity

def updateCartItemInc(item, quantity):
    item['quantity'] += quantity
    item['sum'] += float(item['price']) * quantity

def updateCartTotal(request):
    request.session['total'] = float(0)
    request.session['count'] = int(0)
    for item in request.session['cart']:
        request.session['total'] += item['sum']
        request.session['count'] += item['quantity']

# Create your views here.
def root(request):
    return redirect('amadon/')
def index(request):
    data = {
        'items' :   Item.objects.all()
    }

    return render(request, 'index.html', data)

def addProduct(request, id):
    if 'cart' not in request.session:
        request.session['cart'] = []
        request.session['gTotal'] = float(0)
        request.session['gCount'] = int(0)

    cart = request.session['cart']
    product = Item.objects.get(id=id)
    print(float(product.price))

    found_enable = False
    if cart:
        for item in cart:
            if item['itemID'] == id:
                updateCartItemInc(item, int(request.POST['quantity']))
                found_enable = True
    
    if not found_enable:
        cartItem = {
            'itemID'    :   product.id,
            'itemLink'  :   product.image_link,
            'itemName'  :   product.name,
            'quantity'  :   int(request.POST['quantity']),
            'price'     :   float(product.price),
            'sum'       :   float(product.price) * int(request.POST['quantity'])
        }
        cart.append(cartItem)

    print("Second: ", cart)
    request.session['cart'] = cart
    

    return redirect('/amadon/cart/')

def updateProduct(request, id):
    if 'cart' not in request.session:
        return redirect('/')
    
    cart = request.session['cart']
    if cart:
        for item in cart:
            if item['itemID'] == id:
                updateCartItem(item, int(request.POST['quantity']))
    
    request.session['cart'] = cart
    
    return redirect('/amadon/cart/')

def deleteProduct(request, id):
    if 'cart' not in request.session:
        return redirect('/')
    
    cart = request.session['cart']
 
def cart(request):
    data = {}

    if 'cart' in request.session:
        updateCartTotal(request)
        data = {
            'cart'      :   request.session['cart'],
            'total'     :   request.session['total'],
            'count'     :   request.session['count'],
        }
        
    return render(request, 'cart.html', data)

def checkout(request):
    data = {}

    if 'cart' in request.session:
        request.session['gTotal'] += request.session['total']
        request.session['gCount'] += request.session['count']
        data = {
            'total'     :   request.session['total'],
            'count'     :   request.session['count'],
            'gTotal'    :   request.session['gTotal'],
            'gCount'    :   request.session['gCount'],
        }
        request.session.pop('cart')
        request.session.pop('total')
        request.session.pop('count')

        return render(request, 'checkout.html', data)
    return redirect('/')