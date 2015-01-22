from django.http import HttpResponse
from controller.models import Pin
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def turn(request):
    response_data = {}
    pin_number = request.POST.get('pin', None)
    status     = request.POST.get('status', None)

    # TODO: Verification in forms.py
    pin_number = int(pin_number)
    if status == '1':
        status = True
    else:
        status = False

    pin = Pin()
    pin.turn(pin_number, status)

    response_data['result'] = 'success'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
