from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RegisterView, ReviewCreateView, ReviewListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/<int:pk>/reviews/', ReviewCreateView.as_view()),
    path('products/<int:pk>/reviews/list/', ReviewListView.as_view()),
]
