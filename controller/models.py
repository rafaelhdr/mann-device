from django.conf import settings

class Pin():
    """
    Given an pin, can set the status
    """
    status = False

    def turn(self, pin_number, signal):
        self.status = signal
        handle1 = open(settings.BASE_DIR + '/pins/pin' + str(pin_number) + '.txt','w')
        handle1.write(str(signal))
        handle1.close()
