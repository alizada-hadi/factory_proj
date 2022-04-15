from django.urls import path
from . import views


urlpatterns = [
    path("customers/list/", views.customer_list_view, name="customer-list"), 
    path("customer/create/", views.customer_create_view, name="customer-create"), 
    path("customer/update/<str:pk>/", views.customer_update_view, name="customer-update"), 
    path("customer/delete/<str:pk>/", views.customer_delete_view, name="customer-delete"), 
    path("customer/<str:pk>/order/create/", views.customer_order_view, name="customer-order-create"),

    path("customer/<str:pk>/report/", views.customer_report_view, name="customer-report"), 
    path("customer/event/<str:pk>/update/", views.customer_event_update_view, name="update-event"), 
    path("customer/event/<str:pk>/delete/", views.customer_event_delete_view, name="event-delete"),
     
    path("customer/<str:pk>/add/finance/", views.add_finance_detail_view, name="add-finance-detail"), 

    # update and delete order
    path("order/edit/", views.update_order_view, name="update-order"), 
    path("order/delete/", views.delete_order_view, name="order-delete")
]