from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import date

# Create your views here.
URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
API_KEY = 'GCEbouJZVDpfepDSHYSHKEKFmI6JM7js'

@api_view(['GET'])
def api_test(request):
    url = URL
    params = {
        'authkey': API_KEY,
        'data': 'AP01'  # AP01 : 환율 정보
    }
    response = requests.get(url, params=params).json()
    return Response(response)


@api_view(['GET'])
def save_rate(request):
    url = URL
    params = {
        'authkey': API_KEY,
        'data': 'AP01'  # AP01 : 환율 정보
    }
    response = requests.get(url, params=params).json()

    today = date.today()

    # for rate_data in response:
        # deal_bas_r = parseFloat(rate_data['deal_bas_r'])