from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('autenthication/token/', TokenObtainPairView.as_view(), name="token_obtain_pais"),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name="token_refesh"),
]