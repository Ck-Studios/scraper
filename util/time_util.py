from random import gauss
from time import sleep as original_sleep

# Amount of variance to be introduced
# i.e. random time will be in the range: TIME +/- STDEV %
STDEV = 0.5
sleep_percentage = 1


def randomize_time(mean):
    allowed_range = mean * STDEV
    stdev = allowed_range / 3  # 99.73% chance to be in the allowed range

    t = 0
    while abs(mean - t) > allowed_range:
        t = gauss(mean, stdev)

    return t


def set_sleep_percentage(percentage):
    global sleep_percentage
    sleep_percentage = percentage/100


def sleep(t, custom_percentage=None):
    if custom_percentage is None:
        custom_percentage = sleep_percentage
    time = randomize_time(t)*custom_percentage
    original_sleep(time)

def sleep_actual(t):
  original_sleep(t)
