from django.urls import path

from customer.views import register_view, MyTokenObtainPairView
from wallet.views import secure_view

urlpatterns = [
    path('api/v1/auth/register', register_view, name='register'),
    path('api/v1/auth/token', MyTokenObtainPairView.as_view(), name='token'),
    path('api/v1/wallet/secure', secure_view, name='token'),
]
