from django.urls import path
from . import views

urlpatterns = [
     path('orders/',views.OrderCreateListView.as_view(),name='orders'),
     path('order/<int:order_id>/',views.OrderDetailView.as_view(),name='order_detail'),
     path('update-status/<int:order_id>/',views.UpdateOrderStatus.as_view(),name='update_order_status'),
     path('orders/user/<int:user_id>/order/',views.UserOrdersView.as_view(),name='users_orders'),
     path('orders/user/<int:user_id>/order/<int:order_id>/',views.UserOrderDetailView.as_view(),name='user_order_detail'),

]