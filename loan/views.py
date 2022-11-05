import json
import uuid

from datetime import date, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view



# Create your views here.
loans = [
    {
        "uuid": str(uuid.uuid4()),
        "name": "ICICI VALUE-X01",
        "value": "40000",
        "due_date": str(date.today() + timedelta(days=10))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "HDFC MSME-R45",
        "value": "24000",
        "due_date": str(date.today() + timedelta(days=14))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "IDFC FIRST T50",
        "value": "37499",
        "due_date": str(date.today() + timedelta(days=21))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "HDFC MIL T23",
        "value": "10999",
        "due_date": str(date.today() + timedelta(days=30))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "ICICI VALUE-X01",
        "value": "40000",
        "due_date": str(date.today() + timedelta(days=10))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "PNB PRO MSME-R45",
        "value": "24000",
        "due_date": str(date.today() + timedelta(days=14))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "SBI SAFAR T50",
        "value": "37499",
        "due_date": str(date.today() + timedelta(days=21))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "IDFC T23",
        "value": "10999",
        "due_date": str(date.today() + timedelta(days=30))
    }
]


def get_loans(request):
    resp = {
        "loans": loans
    }
    return JsonResponse(resp)


@csrf_exempt
# @api_view(['POST'])
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