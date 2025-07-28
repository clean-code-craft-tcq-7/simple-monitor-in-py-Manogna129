from time import sleep
import sys

def blink_alert(times=6, delay=1):
    """Display a blinking asterisk animation."""
    for _ in range(times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)

def vitals_ok(temperature, pulseRate, spo2):
    checks = [
        (temperature > 102 or temperature < 95, 'Temperature critical!'),
        (pulseRate < 60 or pulseRate > 100, 'Pulse Rate is out of range!'),
        (spo2 < 90, 'Oxygen Saturation out of range!')
    ]
    
    for condition, message in checks:
        if condition:
            print(message)
            blink_alert()
            return False
    return True
