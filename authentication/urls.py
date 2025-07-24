from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('autenthication/token/', TokenObtainPairView.as_view(), name="token_obtain_pais"),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name="token_refesh"),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
]