from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, libro, quantity=0, action=None):
        """
        Agrega productos al carro o actualizar cantidad.
        """
        id = libro.isbn
        newItem = True
        if str(libro.isbn) not in self.cart.keys():

            self.cart[libro.isbn] = {
                #'userid': self.request.user.id,
                'product_id': id,
                'name': libro.titulo,
                'quantity': 1,
                'price': str(libro.precio),
                'image': libro.portada.url
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(libro.isbn):
                    value['quantity'] = value['quantity']
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[libro.isbn] = {
                #'userid': self.request.user.id,
                'product_id': id,
                'name': libro.titulo,
                'quantity': 1,
                'price': str(libro.precio),
                'image': libro.portada.url
            }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, libro):
        """
        Elimina productos del carro.
        """
        product_id = str(libro.isbn)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def increment(self, libro):
        for key, value in self.cart.items():
            if key == str(libro.isbn):
                value['quantity'] = value['quantity'] + 1
                self.save()
                break

    def decrement(self, libro):
        for key, value in self.cart.items():
            if key == str(libro.isbn):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
