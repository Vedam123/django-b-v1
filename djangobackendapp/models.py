from django.db import models
from datetime import date

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining= models.DateField()
    PhotoFileName = models.CharField(max_length=100)
    
class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100)
    ProductCategory = models.CharField(max_length=100)
    ProductUOM = models.CharField(max_length=10)   
    CostPrice= models.FloatField()
    SalesPrice=models.FloatField()
    PhotoFileName = models.CharField(max_length=100)
    
class Inventory(models.Model):
    InventoryId = models.AutoField(primary_key=True)
    InventoryLocationName = models.CharField(max_length=100)
    ProductId = models.PositiveIntegerField()
    ProductName = models.CharField(max_length=100)
    CycleCounting = models.PositiveIntegerField()
    ProductUOM = models.CharField(max_length=10)  
    AvalableQuantity= models.PositiveIntegerField()
    ReceivedQuantity=models.PositiveIntegerField()
    SoldQuantity=models.PositiveIntegerField()
    
class Sales(models.Model):
    SalesOrderId = models.AutoField(primary_key=True)
    CustomerNumber = models.PositiveIntegerField()
    CustomerName = models.CharField(max_length=100)
    ProductId = models.PositiveIntegerField()
    ProductName = models.CharField(max_length=100)
    ProductUOM = models.CharField(max_length=10)
    SalesQuantity=models.PositiveIntegerField()
    SalesPrice=models.FloatField()
    Amount=models.FloatField()
    SalesOrderDate= models.DateField(default=date.today)
    
class Customers(models.Model):
    CustomerNumber = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=100)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    Street = models.CharField(max_length=50) 
    City = models.CharField(max_length=30)
    Country =   models.CharField(max_length=30)
    PhoneNumber = models.PositiveIntegerField()
    Language =   models.CharField(max_length=30)
    Created= models.DateField(default=date.today)
    Status= models.BooleanField()
    Discount = models.PositiveIntegerField()