import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger('walletmanager.logger')
JSON_PARAMS = {'indent': 2}


@csrf_exempt
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def secure_view(request):
    data = {"message": "Access Granted"}
    return JsonResponse(data, json_dumps_params=JSON_PARAMS)
