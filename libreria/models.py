from django.db import models

from django.contrib.auth.models import User

class Autores(models.Model):
    id_autor = models.IntegerField(primary_key=True)
    apellidos = models.CharField(max_length=25)
    nombres = models.CharField(max_length=25)

    def __str__(self):
        return '{} - {} {}'.format(
            self.id_autor,
            self.apellidos,
            self.nombres
        )
    
    def save(self):
        self.apellidos = self.apellidos.title()
        self.nombres = self.nombres.title()
        super(Autores, self).save()

    class Meta:
        db_table = 'autores'
        verbose_name_plural = "Autores"


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=40)

    def __str__(self):
        return '{} - {}'.format(
            self.id_categoria,
            self.categoria
        )
    
    def save(self):
        self.categoria = self.categoria.capitalize()
        super(Categorias, self).save()

    class Meta:
        db_table = 'categorias'
        verbose_name_plural = "Categorias"


class Clientes(models.Model):
    id_clientes = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    correo_electronico = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format( 
            self.id_clientes,
            self.identificacion,
            self.nombres,
            self.apellidos,
            self.telefono,
            self.direccion,
            self.correo_electronico
        )

    def save(self):
        self.apellidos = self.apellidos.title()
        self.nombres = self.nombres.title()
        super(Clientes, self).save()

    class Meta:
        db_table = 'clientes'
        verbose_name_plural = "Clientes"


class Libros(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=128)
    fecha_pub = models.DateField()
    categoria = models.ForeignKey(Categorias, db_column='categoria', on_delete=models.CASCADE)
    precio = models.IntegerField()
    portada = models.ImageField(blank=True, null=True, upload_to="portadas")

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.isbn,
            self.titulo,
            self.fecha_pub,
            self.categoria,
            self.precio,
            self.portada
        )
    
    def save(self):
        self.titulo = self.titulo.capitalize()
        super(Libros, self).save()

    class Meta:
        db_table = 'libros'
        verbose_name_plural = "Libros"


class LibrosPorAutor(models.Model):
    id_autor = models.OneToOneField(Autores, db_column='id_autor', on_delete=models.CASCADE, primary_key=True)
    isbn = models.ForeignKey(Libros, db_column='isbn', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(
            self.id_autor,
            self.isbn
        )

    class Meta:
        db_table = 'libros_por_autor'
        verbose_name_plural = "Libros Por Autores"


class PedidosCliente(models.Model):
    nro_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, db_column='id_cliente', on_delete=models.CASCADE)
    isbn = models.ForeignKey(Libros, db_column='isbn', on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format( 
            self.nro_pedido,
            self.id_cliente.nombres + self.id_cliente.apellidos,
            self.isbn.titulo,
            self.fecha_pedido,
            self.cantidad,
            self.valor,
        )

    class Meta:
        db_table = 'pedidos_cliente'
        verbose_name_plural = "Pedidos Por Clientes"

