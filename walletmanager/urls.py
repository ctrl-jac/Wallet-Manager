from django.urls import path

from customer.views import register_view, MyTokenObtainPairView
from wallet.views import secure_view, wallet_view

urlpatterns = [
    path('api/v1/auth/register', register_view, name='register'),
    path('api/v1/init', MyTokenObtainPairView.as_view(), name='token'),
    path('api/v1/wallet', wallet_view, name='wallet'),
    path('api/v1/wallet/deposit', secure_view, name='deposit'),
    path('api/v1/wallet/withdrawal', secure_view, name='withdrawal'),
]
