from django.db import models

# Create your models here.

class Benefactor(models.Model):
    id = models.AutoField(primary_key=True)
    NombreCompleto = models.CharField(max_length=100, null=False) 
    Email = models.CharField(max_length=100, null=False)
    Telefono = models.CharField(max_length=10, null=False)
    UbicacionDomicilio = models.CharField(max_length=100, null=False)
    Anonimo = models.BooleanField(default=False, null=True)
    def __str__(self):
        return self.NombreCompleto
    
class InstitucionAsilo(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    NIT = models.CharField(max_length=20)
    NombreRepresentantePrincipal = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    Celular = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=200)
    Localizacion = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre

class Campania(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Requerimiento = models.CharField(max_length=100, null=False)
    Imagenes = models.TextField(null=False)
    FechaInicio = models.DateTimeField(null=False)
    FechaCierre = models.DateTimeField(null=False)
    Estado = models.BooleanField(default=True, null=False)
    InstitucionAsiloID =models.IntegerField(null=False)
    InstitucionAsilo = models.ForeignKey(InstitucionAsilo, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre

class Donacion(models.Model):
    id = models.AutoField(primary_key=True)
    CampaniaID = models.IntegerField(null=False)
    BenefactorID = models.IntegerField(null=False)
    RecogidaPorAsilo = models.BooleanField(default=False, null=False)
    FechaRecoleccion = models.DateTimeField(null=False)
    RecibidoPorAsilo = models.BooleanField(default=False, null=False)
    Campania = models.ForeignKey(Campania, on_delete=models.CASCADE)
    Benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    def __str__(self):
        return self.id
    
class Gestor(models.Model):
    id = models.AutoField(primary_key=True)
    Usuario = models.CharField(max_length=50, null=False)
    Password = models.CharField(max_length=50, null=False)
    Email = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.Usuario
    
class RecojosProgramados(models.Model):
    id = models.AutoField(primary_key=True)
    CampaniaID = models.IntegerField(null=False)
    FechaRecoleccion = models.DateTimeField(null=False)
    Responsable = models.CharField(max_length=100, null=False)
    Campania = models.ForeignKey(Campania, on_delete=models.CASCADE)
    def __str__(self):
        return self.id
    