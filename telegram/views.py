from rest_framework import viewsets
from .models import TelegramUser
from .serializers import TelegramUserSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer


@csrf_exempt
def telegram_update(request):
    if request.method == "POST":
        update = json.loads(request.body)
        user_data = update.get('message', {}).get('from')
        if user_data:
            TelegramUser.objects.update_or_create(
                telegram_id=user_data['id'],
                defaults={
                    'first_name': user_data.get('first_name'),
                    'last_name': user_data.get('last_name'),
                    'username': user_data.get('username'),
                }
            )
        return JsonResponse({"ok": True})
    return JsonResponse({"error": "Method not allowed"}, status=405)