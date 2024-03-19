from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelegramUserViewSet, telegram_update


router = DefaultRouter()
router.register(r'users', TelegramUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('webhook/', telegram_update, name='telegram_webhook'),
]