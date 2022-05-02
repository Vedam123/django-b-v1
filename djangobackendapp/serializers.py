from rest_framework import serializers
from djangobackendapp.models import Employees, Departments,Inventory,Products,Sales,Customers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')
        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('InventoryId',
                  'InventoryLocationName',
                  'ProductId',
                  'ProductName',
                  'CycleCounting',
                  'ProductUOM',
                  'AvalableQuantity',
                  'ReceivedQuantity',
                  'SoldQuantity')
        
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('ProductId',
                  'ProductName',
                  'ProductCategory',
                  'ProductUOM',
                  'CostPrice',
                  'SalesPrice',
                  'PhotoFileName')
        
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('SalesOrderId',
                  'CustomerNumber',
                  'CustomerName',
                  'ProductId',
                  'ProductName',
                  'ProductUOM',
                  'SalesQuantity',
                  'SalesPrice',
                  'Amount',
                  'SalesOrderDate')
        
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('CustomerNumber',
                  'CustomerName',
                  'Email',
                  'Address',
                  'Street',
                  'City',
                  'Country',
                  'PhoneNumber',
                  'Language',
                  'Created',
                  'Status',
                  'Discount')        