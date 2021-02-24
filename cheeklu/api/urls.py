from .views.user_views import AddUser, LoginUser
from .views.product_views import AddProduct, GetProduct
from django.urls import path

urlpatterns = [
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('get-product/<str:name>/', GetProduct.as_view(), name='get-product'),
    path('add-user/', AddUser.as_view(), name='add-user'),
    path('login-user/', LoginUser.as_view(), name='login-user'),
]
