import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from transaction.models import Transaction
from wallet.models import Wallet

logger = logging.getLogger('walletmanager.logger')
JSON_PARAMS = {'indent': 2}


@csrf_exempt
@api_view(['POST', 'GET', 'PATCH', ])
@permission_classes([IsAuthenticated])
def wallet_view(request):
    response_data = {'status': '', 'data': {}, 'message': []}
    customer = request.user
    wallet = None
    try:
        wallet = Wallet.objects.get(customer=customer)
    except ObjectDoesNotExist as e:
        response_data['status'] = 'FAILED'
        response_data['message'].append('Unable to Find Wallet For Customer')
        return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)

    if request.method == 'POST':
        if wallet.status is True:
            response_data['status'] = 'FAILED'
            response_data['message'].append('Wallet Already Enabled')
        else:
            wallet.status = True
            wallet.enabled_at = timezone.now()
            try:
                wallet.save()
                response_data['status'] = 'SUCCESS'
                response_data['data'] = {'wallet': wallet.get_dict()}
                response_data['message'].append('Wallet Enabled')
            except ValueError as e:
                logger.error('Error in Save : DB Error' + str(e.args[0]))
                response_data['status'] = 'FAILED'
                response_data['message'].append('Database Error')
        return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)
    if request.method == 'PATCH':
        is_disabled_flag = request.data.get('is_disabled', '')
        if is_disabled_flag and is_disabled_flag.lower() == 'true':
            if wallet.status is False:
                response_data['status'] = 'FAILED'
                response_data['message'].append('Wallet Already Disabled')
            else:
                wallet.status = False
                try:
                    wallet.save()
                    response_data['status'] = 'SUCCESS'
                    response_data['data'] = {'wallet': wallet.get_dict()}
                    response_data['message'].append('Wallet Disabled')
                except ValueError as e:
                    logger.error('Error in Save : DB Error' + str(e.args[0]))
                    response_data['status'] = 'FAILED'
                    response_data['message'].append('Database Error')
        else:
            response_data['status'] = 'FAILED'
            response_data['message'].append('Form Data (is_disabled) Missing/Invalid')
        return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)
    if request.method == 'GET':
        if wallet.status is False:
            response_data['status'] = 'FAILED'
            response_data['message'].append('Operation Not permitted. Wallet is Disabled')
        else:
            response_data['status'] = 'SUCCESS'
            response_data['data'] = {'wallet': wallet.get_dict()}
        return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)


@csrf_exempt
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def reference_view(request):
    response_data = {'status': '', 'data': {}, 'message': []}
    customer = request.user
    wallet = None
    try:
        wallet = Wallet.objects.get(customer=customer)
    except ObjectDoesNotExist as e:
        response_data['status'] = 'FAILED'
        response_data['message'].append('Unable to Generate ReferenceID. No Wallet Found.')
        return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)

    if wallet.status is False:
        response_data['status'] = 'FAILED'
        response_data['message'].append('Wallet is Disabled. Transaction not Permitted.')
    else:
        transaction = Transaction(wallet=wallet)
        try:
            transaction.save()
            response_data['status'] = 'SUCCESS'
            response_data['data'] = transaction.get_dict()
            response_data['message'].append('Reference ID Generated for Transaction.')
        except ValueError as e:
            logger.error('Error in Save : DB Error' + str(e.args[0]))
            response_data['status'] = 'FAILED'
            response_data['message'].append('Database Error')
    return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)


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








