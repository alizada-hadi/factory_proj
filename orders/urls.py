from django.urls import path
from . import views


urlpatterns = [
    path("order/update/<str:pk>/", views.order_update_view, name="order-update"), 
    path("order/delete/<str:pk>/", views.order_delete_view, name="delete-order")
]