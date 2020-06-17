from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Autores, Categorias, Clientes, Libros, \
    LibrosPorAutor, PedidosCliente
from .forms import AutoresForm, CategoriasForm, LibrosForm, \
    LibrosPorAutorForm, ClientesForm
from django.db.models import Q

# Decoradores
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .cart import Cart


class Sinprivilegios(SuccessMessageMixin, LoginRequiredMixin, \
    PermissionRequiredMixin):
    login_url = 'lib:login'
    raise_exception = False
    redirect_field_name = "redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='lib:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(generic.TemplateView):
    template_name = 'libreria/index.html'


class HomeSinPrivilegios(generic.TemplateView):
    template_name = "libreria/sin_privilegios.html"


def listar_autores(request):
    busqueda = request.POST.get("buscar")
    autores = Autores.objects.all()

    if busqueda:
        autores = Autores.objects.filter(
            Q(id_autor__icontains = busqueda) | 
            Q(apellidos__icontains = busqueda) |
            Q(nombres__icontains = busqueda) 
        ).distinct()
         
    return render(request, 'libreria/autores_list.html', {'autores':autores})


class AutoresNew(Sinprivilegios, generic.CreateView):
    permission_required = "libreria.add_autores"
    model = Autores
    template_name = "libreria/autores_form.html"
    context_object_name = "obj"
    form_class = AutoresForm
    success_url = reverse_lazy('lib:autores')
    success_message = "Autor Creado Satisfactoriamente"


class AutoresEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "libreria.change_autores"
    model = Autores
    temlate_name = "libreria/autores_form.html"
    context_object_name = "obj"
    form_class = AutoresForm
    success_url = reverse_lazy('lib:autores')
    success_message = "Autor Actualizado Satisfactoriamente"


class AutoresDel(Sinprivilegios, generic.DeleteView):
    permission_required = "libreria.delete_autores"
    model = Autores
    template_name = "libreria/libreria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('lib:autores')
    success_message = "Autor Eliminado Satisfactoriamente"


def listar_libros(request):
    busqueda = request.POST.get("buscar")
    libros = Libros.objects.all()

    if busqueda:
        libros = Libros.objects.filter(
            Q(isbn__icontains = busqueda) | 
            Q(titulo__icontains = busqueda) |
            Q(fecha_pub__icontains = busqueda) |
            # Q(categoria__exact = busqueda) |
            Q(precio__icontains = busqueda) 
        ).distinct()
         
    return render(request, 'libreria/libros_list.html', {'libros':libros})

class LibrosNew(Sinprivilegios, generic.CreateView):
    permission_required = "libreria.add_libros"
    model = Libros
    template_name = "libreria/libros_form.html"
    context_object_name = "obj"
    form_class = LibrosForm
    success_url = reverse_lazy('lib:libros')
    success_message = "Libro Creado Satisfactoriamente"


class LibrosEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "libreria.change_libros"
    model = Libros
    template_name= "libreria/libros_form.html"
    context_object_name = "obj"
    form_class = LibrosForm
    success_url = reverse_lazy('lib:libros')
    success_message = "Libro Actualizado Satisfactoriamente"


class LibrosDel(Sinprivilegios, generic.DeleteView):
    permission_required = "libreria.delete_libros"
    model = Libros
    template_name = "libreria/libreria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('lib:libros')
    success_message = "Libro Eliminado Satisfactoriamente"


def listar_categorias(request):
    busqueda = request.POST.get("buscar")
    categorias = Categorias.objects.all()

    if busqueda:
        categorias = Categorias.objects.filter(
            Q(id_categoria__icontains = busqueda) | 
            Q(categoria__icontains = busqueda) 
        ).distinct()
         
    return render(request, 'libreria/categorias_list.html', {'categorias': categorias})

class CatgeoriasNew(Sinprivilegios, generic.CreateView):
    permission_required = "libreria.add_categorias"
    model = Categorias
    template_name = "libreria/categorias_form.html"
    context_object_name = "obj"
    form_class = CategoriasForm
    success_url = reverse_lazy('lib:categorias')
    success_message = "Categoria Creada Satisfactoriamente"


class CategoriaEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "libreria.change_categorias"
    model = Categorias
    template_name = "libreria/categorias_form.html"
    context_object_name = "obj"
    form_class = CategoriasForm
    success_url = reverse_lazy('lib:categorias')
    success_message = "Categoria Actualizada Satisfactoriamente"


class CategoriaDel(Sinprivilegios, generic.DeleteView):
    permission_required = "libreria.delete_categorias" 
    model = Categorias
    template_name = "libreria/libreria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('lib:categorias')
    success_message = "Categoria Eliminada Satisfactoriamente"


@login_required(login_url='/login/')
@permission_required('libreria.view_clientes', login_url='lib:sin_privilegios')
def listar_clientes(request):
    busqueda = request.POST.get("buscar")
    clientes = Clientes.objects.all()

    if busqueda:
        clientes = Clientes.objects.filter(
            Q(id_clientes__icontains = busqueda) | 
            Q(identificacion__icontains = busqueda) |
            Q(nombres__icontains = busqueda) |
            Q(apellidos__icontains = busqueda) |
            Q(telefono__icontains = busqueda) |
            Q(direccion__icontains = busqueda) 
        ).distinct()
         
    return render(request, 'libreria/clientes_list.html', {'clientes': clientes})


class ClientesNew(Sinprivilegios, generic.CreateView):
    permission_required = "libreria.add_clientes"
    model = Clientes
    template_name = "libreria/clientes_form.html"
    context_object_name = "obj"
    form_class = ClientesForm
    success_url = reverse_lazy('lib:clientes')
    success_message = "Cliente Creado Satisfactoriamente"


class ClientesEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "libreria.change_clientes"
    model = Clientes
    template_name = "libreria/clientes_form.html"
    context_object_name = "obj"
    form_class = ClientesForm
    success_url = reverse_lazy('lib:clientes')
    success_message = "Cliente Actualizado Satisfactoriamente"


class ClientesDel(Sinprivilegios, generic.DeleteView):
    permission_required = "libreria.delete_clientes" 
    model = Clientes
    template_name = "libreria/libreria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('lib:clientes')
    success_message = "Categoria Eliminada Satisfactoriamente"


def listar_libros_por_autor(request):
    busqueda = request.POST.get("buscar")
    librosXautor = LibrosPorAutor.objects.all()

    if busqueda:
        librosXautor = Categorias.objects.filter(
            Q(id_autor__exact  = busqueda) | 
            Q(idbn__exact = busqueda) 
        ).distinct()
         
    return render(request, 'libreria/libros_por_autor_list.html', {'librosXautores': librosXautor})


class LibrosPorAutorNew(Sinprivilegios, generic.CreateView):
    permission_required = "libreria.add_librosporautor"
    model = LibrosPorAutor
    template_name = "libreria/libros_por_autor_form.html"
    context_object_name = "obj"
    form_class = LibrosPorAutorForm
    success_url = reverse_lazy('lib:libros_por_autor')
    success_message = "Libro Por Autor Creado Correctamente"


class LibrosPorAutorEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "libreria.change_librosporautor"
    model = LibrosPorAutor
    template_name = "libreria/libros_por_autor_form.html"
    context_object_name = "obj"
    form_class = LibrosPorAutorForm
    success_url = reverse_lazy('lib:libros_por_autor')
    success_message = "Libro Por Autor Actualiado Correctamente"


class LibrosPorAutorDel(Sinprivilegios, generic.DeleteView):
    permission_required = "libreria.delete_librosporautor"
    model = LibrosPorAutor
    template_name = "libreria/libreria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('lib:libros_por_autor')
    success_message = "Autor Eliminado Satisfactoriamente"


@login_required(login_url='/login/')
@permission_required('libreria.view_pedidoscliente', login_url='lib:sin_privilegios')
def listar_pedidos_clientes(request):
    busqueda = request.POST.get("buscar")
    pedidos_clientes = PedidosCliente.objects.all()

    if busqueda:
        pedidos_clientes = PedidosCliente.objects.filter(
            Q(nro_pedido__icontains = busqueda) | 
            # Q(id_cliente__exact = busqueda) |
            # Q(isbn__exact = busqueda) |
            Q(fecha_pedido__icontains = busqueda) | 
            Q(cantidad__icontains = busqueda) | 
            Q(valor__icontains = busqueda) 
        ).distinct()
         
    return render(request, 'libreria/pedidosclientes_list.html', {'pedidos_clientes': pedidos_clientes})

# Funciones de carrito de compras
def cart_add(request, isbn):
    cart = Cart(request)
    libro = Libros.objects.get(isbn=isbn)
    cart.add(libro=libro)
    return redirect("lib:libros")

def item_clear(request, isbn):
    cart = Cart(request)
    libro = Libros.objects.get(isbn=isbn)
    cart.remove(libro)
    return redirect("lib:cart_detail")

def item_increment(request, isbn):
    cart = Cart(request)
    libro = Libros.objects.get(isbn=isbn)
    cart.increment(libro=libro)
    return redirect("lib:cart_detail")

def item_decrement(request, isbn):
    cart = Cart(request)
    libro = Libros.objects.get(isbn=isbn)
    cart.decrement(libro=libro)
    return redirect("lib:cart_detail")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("lib:cart_detail")

def cart_detail(request):
    return render(request, 'libreria/carro.html')

