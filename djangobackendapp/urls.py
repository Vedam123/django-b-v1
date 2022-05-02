#from django.conf.urls import url
from django.urls import path, re_path
from djangobackendapp import views
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls.static import static
from django.conf import settings

#urlpatterns=[path('list/departments',views.departmentApi),
#             path('create/department', views.departmentApi),
#             path('delete/department/<int:Id>', views.departmentApi),
#             path('update/department/<int:Id>', views.departmentApi)
#]

urlpatterns=[
    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),
    re_path(r'^employee/saveFile$', csrf_exempt(views.saveFile)),
    path('showEmployees', views.display_images), 
    path('sales', views.salesApi), 
    path('inventory/', views.inventoryApi), 
    path('products/', views.productsApi),
    path('products/saveFile', csrf_exempt(views.saveFile)), 
    path('customers', views.customersApi)            
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)