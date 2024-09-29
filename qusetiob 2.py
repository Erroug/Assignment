# Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Answer: Yes, by default Django signals run in the same thread as the caller.

import threading
import datetime
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def handle_signal(sender, **kwargs):
    print("Signal received at:", datetime.datetime.now())
    print("Handler thread ID:", threading.get_ident())

def send_signal():
    print("Sending signal at:", datetime.datetime.now())
    print("Sender thread ID:", threading.get_ident())
    my_signal.send(sender=None)

send_signal()
