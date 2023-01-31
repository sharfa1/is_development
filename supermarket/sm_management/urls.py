from django.urls import path
from . import views




app_name='sm_management'
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('customer view',views.customer_view,name='customer view'),
    path('customer list',views.customer_list,name='customer list'),
    path('about',views.home,name='about')
  
]
