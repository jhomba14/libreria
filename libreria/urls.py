from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import Home, HomeSinPrivilegios, \
    AutoresNew, AutoresEdit, AutoresDel, \
    CatgeoriasNew, CategoriaEdit, CategoriaDel, \
        LibrosNew, LibrosEdit, LibrosDel, \
            LibrosPorAutorNew, LibrosPorAutorEdit, LibrosPorAutorDel, \
                ClientesNew, ClientesEdit, ClientesDel

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('sin_privilegios/',HomeSinPrivilegios.as_view(),name='sin_privilegios'),

    # Urls de acceso
    path('login/',auth_views.LoginView.as_view(template_name='cuentas/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='cuentas/login.html'),name='logout'),
    path('cambiar-contraseña/', auth_views.PasswordChangeView.as_view(template_name='cuentas/cambiar.html'), name='cambiar_contraseña'),
    path('cambiar-contraseña/completo/', auth_views.PasswordChangeDoneView.as_view(template_name='cuentas/cambiado.html'), name='cambiado'),

    # Urls libreria
    # Urls Autores
    path('autores/', views.listar_autores, name="autores"),
    path('autores/new/', AutoresNew.as_view(), name="autores_new"),
    path('autores/edit/<pk>', AutoresEdit.as_view(), name="autores_edit"),
    path('autores/delete/<pk>', AutoresDel.as_view(), name="autores_delete"),

    # Urls de libros
    path('libros/', views.listar_libros, name="libros"),
    path('libros/new/', LibrosNew.as_view(), name="libros_new"),
    path('libros/edit/<int:pk>', LibrosEdit.as_view(), name="libros_edit"),
    path('libros/delete/<int:pk>', LibrosDel.as_view(), name="libros_delete"),

    # Urls Categorias
    path('categorias/', views.listar_categorias, name="categorias"),
    path('categorias/new/', views.CatgeoriasNew.as_view(), name="categorias_new"),
    path('categorias/edit/<pk>', views.CategoriaEdit.as_view(), name="categorias_edit"),
    path('categorias/delete/<pk>', views.CategoriaDel.as_view(), name="categorias_delete"),

    # Urls Libros Por Autor
    path('libroXautor/', views.listar_libros_por_autor, name="libros_por_autor"),
    path('libroXautor/new/', LibrosPorAutorNew.as_view(), name="libros_por_autor_new"),
    path('libroXautor/edit/<pk>', LibrosPorAutorEdit.as_view(), name="libros_por_autor_edit"),
    path('libroXautor/delete/<pk>', LibrosPorAutorDel.as_view(), name="libros_por_autor_delete"),

    # Urls clients
    path('clientes/', views.listar_clientes, name="clientes"),
    path('clientes/new', ClientesNew.as_view(), name="clientes_new"),
    path('clientes/edit/<int:pk>', ClientesEdit.as_view(), name="clientes_edit"),
    path('clientes/delete/<int:pk>', ClientesDel.as_view(), name="clientes_delete"),

    
    path('pedidos_clientes/', views.listar_pedidos_clientes, name="pedidos_cliente"),


    # Carro de compras
    path('carro/add/<isbn>/', views.cart_add, name='cart_add'),
    path('carro/item_clear/<isbn>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<isbn>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<isbn>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('carro/cart-detail/',views.cart_detail, name='cart_detail')
]
