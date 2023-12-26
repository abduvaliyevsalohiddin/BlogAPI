from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from blogapp.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="25-12-2023 vazifa uchun yozilgan BlogAPI",
        default_version="V1",
        description="Vazifaga",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maqolalar/', MaqolalarAPIView.as_view()),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),

    path('maqola/<int:pk>/', MaqolaAPIView.as_view()),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    # path('docs2/', schema_view.with_ui('redoc', cache_timeout=0)),
]
