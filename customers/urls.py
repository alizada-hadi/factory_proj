from django.urls import path
from . import views


urlpatterns = [
    path("customers/list/", views.customer_list_view, name="customer-list"), 
    path("customer/create/", views.customer_create_view, name="customer-create"), 
    path("customer/update/<str:pk>/", views.customer_update_view, name="customer-update"), 
    path("customer/delete/<str:pk>/", views.customer_delete_view, name="customer-delete")
]