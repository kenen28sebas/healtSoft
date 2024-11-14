from django.db import models

# Create your models here.
class Persona(models.Model):
    nro_doc = models.CharField(max_length=12,primary_key=True,null=False)
    tdoc = [
        ('CC', 'cedula de ciudadania'),
        ('CE', 'cedula de Extranjeria'),
        ('TI', 'Tarjeta de identidad'), 
        ('RC', 'Registro civil'),
        ('PA', 'Pasaporte'),
        ('ASI', 'Adulto sin identificaion'),
        ('MSI', 'Menor sin identificaion'),
    ]
    tipo_doc = models.CharField(max_length=3,null=False, choices=tdoc)
    lugar_exp_doc = models.CharField(max_length=50,null=False)
    fecha_exp_doc = models.DateField( auto_now=False, auto_now_add=False) 
    nombres = models.CharField(max_length=50,null=False, blank=False)
    apellido_1 = models.CharField(max_length=30,null=False, blank=False)
    apellido_2 = models.CharField(max_length=30,null=False, blank=False)
    sex = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('I','Indeterminado')
    ]
    sexo = models.CharField(max_length=1,null=False,choices=sex)
    fecha_nacimiento = models.DateField( auto_now=False, auto_now_add=False)
    ec = [
        ('Soltero','Soltero'),
        ('Casado','Casado'),
        ('Divorciado','Divorciado'),
        ('Viudo','Viudo'),
        ('Union Libre','Union Libre'),
        ('Separado','Separado'),
    ]
    estado_civil = models.CharField(max_length=15,null=False,choices=ec)
    email = models.EmailField(max_length=80,null=False)
    telefono = models.CharField(max_length=15,null=False)
    nacionalidad = models.CharField(max_length=30,null=False)