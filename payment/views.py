from django.shortcuts import render, get_object_or_404, redirect

import json

from django.http import JsonResponse

# Create your views here.

from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from Trainings.models import Trainingsch, Order

from sukhithTproj.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

import razorpay


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))



def payment(request, x):

    currency = "INR"

    trgselected = Trainingsch.objects.get(id=x)

    payment_order = client.order.create(dict(amount=trgselected.Trainingcost, currency=currency))

    payment_order_id = payment_order['id']


    context = {

        'api_key': RAZORPAY_API_KEY,

        'order_id': payment_order_id,

        "trgsel": trgselected,


    }


    return render(request, "payment/razorpay.html",

                  dict(api_key=RAZORPAY_API_KEY, order_id=payment_order_id, trgsel=trgselected))



def complete(request):

    body = json.loads(request.body)

    training = Trainingsch.objects.get(id=body['trgselid'])

    Order.objects.create(RequestedTrainings=training, PaymentID=body['payid'],Requesteduser=request.user)

    return JsonResponse("payment done", safe=False)


@csrf_exempt

def payment_canceled(request):

    return render(request, 'payment/Cancelpay.html')


def paycomplete(request, x):

    context = {'pay': x}

    return render(request, 'payment/paycomplete.html', context)


def payment_process(request):

    host = request.get_host()


    paypal_dict = {

        "business": "sukhithtechnologies@gmail.com",

        "amount": "1000.00",

        "item_name": "adb",

        "invoice": "20",

        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),

        "return": request.build_absolute_uri(reverse('payment:done')),

        "cancel_return": request.build_absolute_uri(reverse('payment:canceled')),

        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)

    }

    return render(request, "payment/payment.html")



def Cancelpay(request, x):

 
    trgrefund = Order.objects.get(id=x)

    refundStat = client.payment.refund(trgrefund.PaymentID)


    if refundStat:

        trgrefund.delete()

    return render(request, "payment/Cancelpay.html")

