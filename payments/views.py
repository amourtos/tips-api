from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import stripe
# secret key ----
stripe.api_key = 'sk_test_51K1uAdAi0rXIClozI0ukH7ZjFrbyZvWf5eat3duErGuSdZA4WFY6kMYtYFdN3Tb0waDPUdkvVU0gLr82AAauQMps00h52htWay'
# Create your views here.


@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000, currency='pln',
        payment_method_types=['card'],
        receipt_email='test@example.com'
    )
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)
