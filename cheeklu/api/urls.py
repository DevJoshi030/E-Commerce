from .views.form_data_views import GetFormData
from .views.tshirt_views import AddTShirt, GetTShirt
from .views.user_views import AddUser, LoginUser
from .views.product_views import AddProduct, GetProduct
from django.urls import path

urlpatterns = [
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('get-product/<str:name>/', GetProduct.as_view(), name='get-product'),
    path('add-tshirt/', AddTShirt.as_view(), name='add-tshirt'),
    path('get-tshirt/<str:name>/', GetTShirt.as_view(), name='get-tshirt'),
    path('add-user/', AddUser.as_view(), name='add-user'),
    path('login-user/', LoginUser.as_view(), name='login-user'),
    path('get-form-data/<str:category>/',
         GetFormData.as_view(), name='get-form-data'),
]
