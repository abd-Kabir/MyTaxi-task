from django.urls import path
from mytaxi_app.views import OrderListView, OrderCreateAPIView, OrderUpdateAPIView


urlpatterns = [
    path('list/', OrderListView.as_view()),
    path('create/', OrderCreateAPIView.as_view()),
    path('update-status/<int:pk>', OrderUpdateAPIView.as_view()),
]


