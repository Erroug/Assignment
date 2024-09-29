# Question 1 - By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Answer: By default Django signals are executed Synchronously.

import time
import datetime
from django.dispatch import Signal, receiver
my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal received at {datetime.datetime.now()}")
    time.sleep(5)  # Simulate time delay of 5 seconds
    print(f"Signal handler finished at {datetime.datetime.now()}")

def send_signal():
    print(f"Signal sent at {datetime.datetime.now()}")
    my_signal.send(sender=None)  # Send the signal
    print(f"Signal processing done at {datetime.datetime.now()}")

send_signal()
