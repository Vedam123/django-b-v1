from django.shortcuts import render, redirect
import logging
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from djangobackendapp.models import Employees, Departments,Inventory,Products,Sales,Customers
from djangobackendapp.serializers import EmployeeSerializer, DepartmentSerializer, InventorySerializer, ProductsSerializer, SalesSerializer,CustomersSerializer

from django.core.files.storage import default_storage

logger = logging.getLogger(__name__)

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Data inserted Succeffully !", safe=False)
        return JsonResponse("Failed to Insert. !", safe=False)
    elif request.method== 'PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully !", safe=False)
        return JsonResponse("Failed to Update !", safe=False)
    elif request.method == 'DELETE':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        #department_serializer = DepartmentSerializer(department, data=department_data)
        #if department_serializer.is_valid():
        department.delete()
        return JsonResponse("Deleted Sucessfuly !", safe=False)
    
# Employee API as below

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Data inserted Succeffully !", safe=False)
        return JsonResponse("Failed to Insert. !", safe=False)
    elif request.method== 'PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        logging.warning('VEDAM EMP ID %s', employee_data['EmployeeId'])
        logging.warning('Employee name %s', employee_data['EmployeeName']) 
        logging.warning('Department %s', employee_data['Department'])
        logging.warning('Doj %s', employee_data['DateOfJoining'])
        logging.warning('PhotoFileName %s', employee_data['PhotoFileName'])               
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        logging.warning('Employee Serializer is initialzied')   
        if employee_serializer.is_valid():
            logging.warning('Employee Serializer valid') 
            employee_serializer.save()
            ## return JsonResponse("Updated Successfully !", safe=False)##
            logging.warning('Employee Serializer Save is done') 
            return JsonResponse("Data updated Succeffully !" ,safe=False)
        return JsonResponse("Failed to Update !", safe=False)
    elif request.method == 'DELETE':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        #employee_serializer = employeeSerializer(employee, data=employee_data)
        #if employee_serializer.is_valid():
        employee.delete()
        return JsonResponse("Deleted Sucessfuly !", safe=False)
    
@csrf_exempt
def inventoryApi(request, id=0):
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        inventory_serializer = InventorySerializer(inventory, many=True)
        return JsonResponse(inventory_serializer.data, safe=False)
    elif request.method == 'POST':
        inventory_data = JSONParser().parse(request)
        inventory_serializer = InventorySerializer(data=inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse("Data inserted Succeffully !", safe=False)
        return JsonResponse("Failed to Insert. !", safe=False)
    elif request.method== 'PUT':
        inventory_data = JSONParser().parse(request)
        inventory=Inventory.objects.get(InventoryId=inventory_data['InventoryId'])
        inventory_serializer = InventorySerializer(inventory, data=inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse("Data updated Succeffully !" ,safe=False)
        return JsonResponse("Failed to Update !", safe=False)
    elif request.method == 'DELETE':
        inventory_data = JSONParser().parse(request)
        inventory=Inventory.objects.get(InventoryId=inventory_data['InventoryId'])
        #employee_serializer = employeeSerializer(employee, data=employee_data)
        #if employee_serializer.is_valid():
        inventory.delete()
        return JsonResponse("Deleted Sucessfuly !", safe=False) 

@csrf_exempt    
def productsApi(request, id=0):
    if request.method == 'GET':
        products = Products.objects.all()
        products_serializer = ProductsSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        products_data = JSONParser().parse(request)
        products_serializer = ProductsSerializer(data=products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Data inserted Succeffully !", safe=False)
        return JsonResponse("Failed to Insert. !", safe=False)
    elif request.method== 'PUT':
        products_data = JSONParser().parse(request)
        products=Products.objects.get(ProductId=products_data['ProductId'])
        products_serializer = ProductsSerializer(products, data=products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Data updated Succeffully !" ,safe=False)
        return JsonResponse("Failed to Update !", safe=False)
    elif request.method == 'DELETE':
        products_data = JSONParser().parse(request)
        products=Products.objects.get(ProductId=products_data['ProductId'])
        #employee_serializer = employeeSerializer(employee, data=employee_data)
        #if employee_serializer.is_valid():
        products.delete()
        return JsonResponse("Deleted Sucessfuly !", safe=False)         

@csrf_exempt
def salesApi(request, id=0):
    if request.method == 'GET':
        sales = Sales.objects.all()
        sales_serializer = SalesSerializer(sales, many=True)
        return JsonResponse(sales_serializer.data, safe=False)
    elif request.method == 'POST':
        sales_data = JSONParser().parse(request)
        logging.warning('CUSTOMER NAME %s', sales_data['CustomerName'])        
        sales_serializer = SalesSerializer(data=sales_data)
        if sales_serializer.is_valid():
            sales_serializer.save()
            return JsonResponse("Data inserted Succeffully !", safe=False)
        return JsonResponse("Failed to Insert. !", safe=False)
    elif request.method== 'PUT':
        sales_data = JSONParser().parse(request)
        sales=Sales.objects.get(SalesOrderId=sales_data['SalesOrderId'])
        sales_serializer = SalesSerializer(sales, data=sales_data)
        if sales_serializer.is_valid():
            sales_serializer.save()
            return JsonResponse("Data updated Succeffully !" ,safe=False)
        return JsonResponse("Failed to Update !", safe=False)
    elif request.method == 'DELETE':
        sales_data = JSONParser().parse(request)
        sales=Sales.objects.get(SalesOrderId=sales_data['SalesOrderId'])
        #employee_serializer = employeeSerializer(employee, data=employee_data)
        #if employee_serializer.is_valid():
        sales.delete()
        return JsonResponse("Deleted Sucessfuly !", safe=False)   
    
@csrf_exempt
def customersApi(request, id=0):
    if request.method == 'GET':
        customers = Customers.objects.all()
        customers_serializer = CustomersSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
    elif request.method == 'POST':
        customers_data = JSONParser().parse(request)
        logging.warning('CUSTOMER NAME %s', customers_data['CustomerName'])        
        customers_serializer = CustomersSerializer(data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Data inserted Succeffully !", safe=False)
        return JsonResponse("Failed to Insert. !", safe=False)
    elif request.method== 'PUT':
        customers_data = JSONParser().parse(request)
        customers=Customers.objects.get(CustomerNumber=customers_data['CustomerNumber'])
        customers_serializer = CustomersSerializer(customers, data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Data updated Succeffully !" ,safe=False)
        return JsonResponse("Failed to Update !", safe=False)
    elif request.method == 'DELETE':
        customers_data = JSONParser().parse(request)
        customers=Customers.objects.get(CustomerNumber=customers_data['CustomerNumber'])
        customers.delete()
        return JsonResponse("Deleted Sucessfuly !", safe=False)  
    
    
@csrf_exempt
def saveFile(request):
    file = request.FILES['file01']
    logging.warning('VEDAM FILE %s', file)
    logging.warning('VEDAM FILE NAME %s', file.name)
    logging.warning('VEDAM path %s', request.path)
    logging.warning('VEDAM path %s', request.get_full_path_info)    
    file_name= default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def display_images(request): 
    # Location of html file : Django-backend-app\nekrektdbenv\lib\site-packages\django\contrib\admin\templates\show.html. 
    allimages = Employees.objects.all()  
    return render(request, 'showEmployeePics.html',{'images' : allimages})