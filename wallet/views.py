import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from wallet.models import Wallet

logger = logging.getLogger('walletmanager.logger')
JSON_PARAMS = {'indent': 2}


@csrf_exempt
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def secure_view(request):
    data = {"message": "Access Granted"}
    wallet = Wallet(name="wallet")
    wallet.save()
    wallet = wallet.get_dict()
    return JsonResponse(wallet, json_dumps_params=JSON_PARAMS)


@csrf_exempt
@api_view(['POST', 'GET', 'PATCH',])
@permission_classes([IsAuthenticated])
def wallet_view(request):
    response_data = {'status': '', 'data': {}}
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'PATCH':
        pass


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def deposit_view(request):
    response_data = {'status': '', 'data': {}}
    pass


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def withdrawal_view(request):
    response_data = {'status': '', 'data': {}}
    pass








