from django import forms

from .models import Autores, Categorias, Libros, \
    LibrosPorAutor, Clientes


class AutoresForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['apellidos','nombres']
        labels = {'apellidos':"Apellidos de Autor",
                'nombres':"Nombres del autor"}
        widget={'apellidos': forms.TextInput,
                'nombres': forms.TextInput}
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['categoria']
        labels = {'categorias': "Categorias de libros"}
        widget = {'categorias': forms.TextInput}
        
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['isbn','titulo','fecha_pub','categoria','precio','portada']
        labels = {'isbn': "ISBN del libro",'titulo': "Titulo del libro", 
                'fecha_pub': "Fecha depublicacion",'precio': "Precio del Libro",
                'portada': "Foto de portada del lirbo"}
        widget = {'isbn': forms.IntegerField, 'titulo': forms.TextInput,
                'fecha_pub': forms.DateField, 'precio': forms.FloatField,
                'portada': forms.ImageField}
        
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
            self.fields['categoria'].empty_label = "Seleccione Categoria"


class LibrosPorAutorForm(forms.ModelForm):
    class Meta:
        model = LibrosPorAutor
        fields = ['id_autor', 'isbn']

        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            self.fields['id_autor'].empty_label = "Seleccione El id del autor"
            self.fields['isbn'].empty_label = "Seleccione El isbn del libro"


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['identificacion','nombres','apellidos','telefono',
                'direccion', 'correo_electronico']
        labels = {'identificacion': "Identificacion del usuario", 'nombres': "Nombre del usuario",
                'apellidos':"Apellidos del usuario", 'telefono':"Telefono del usuario",
                'direccion': "Direccion del usuario", 'correo_electronico':"Correo electronico del usuario"}
        widget = {'identificacion': forms.NumberInput, 'nombres': forms.TextInput,
                'apellidos': forms.TextInput, 'telefono': forms.NumberInput,
                'direccion': forms.TextInput,'correo_electronico': forms.EmailField}
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
