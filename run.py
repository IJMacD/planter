from os import environ
from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioAsyncController
from time import sleep
from argparse import ArgumentParser
import datetime

url = environ.get('FTDI_DEVICE', 'ftdi:///1')

parser = ArgumentParser(prog='Planter', description='Waters plants')
parser.add_argument('duration', type=float)

args = parser.parse_args()

print("Running planter for {0} seconds".format(args.duration))

def debug_print(message):
    print("{0} {1}".format(datetime.datetime.now().isoformat(), message))

gpio = GpioAsyncController()
gpio.configure(url, direction=0xff)
# port = gpio.get_gpio()

debug_print("Connected")

gpio.write(0xff)
debug_print("on")

sleep(args.duration)
gpio.write(0x00)
debug_print("off")

debug_print("Done")