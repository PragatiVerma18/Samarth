import json
import uuid

from datetime import date, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from loan.constants import loans, txns, offers


@csrf_exempt
def get_loans(request):
    resp = {
        "loans": loans
    }
    return JsonResponse(resp)


@csrf_exempt
def add_new_loan(request):
    try:
        body= json.loads(request.body)
        new_loan={
            "uuid": str(uuid.uuid4()),
            "name": body['name'],
            "value": body['value'],
            "due_date": str(date.today() + timedelta(days=body['days']))
        }
        loans.append(new_loan)
        resp = {
            "success": True,
            "uuid": new_loan["uuid"]
        }
        return JsonResponse(resp)
    except Exception as e:
        resp = {
            "success": False,
            "error": repr(e)
        }
        return JsonResponse(resp)
    
@csrf_exempt  
def fetch_txns(request):
    resp = {
        "txns": txns
    }
    return JsonResponse(resp)

@csrf_exempt  
def fetch_offers(request):
    body= json.loads(request.body)
    tenure=body['tenure']
    for item in offers:
        item['tenure']= tenure
    resp = {
        "offers": offers
    }
    return JsonResponse(resp)