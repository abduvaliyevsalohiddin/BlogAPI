from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from blogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maqolalar/', MaqolalarAPIView.as_view()),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),

    path('maqola/<int:pk>/', MaqolaAPIView.as_view()),
]
