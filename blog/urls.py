from rest_framework import routers
from .views import PostViewSet,CommentViewSet
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]