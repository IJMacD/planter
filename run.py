from os import environ
from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioAsyncController
from time import sleep
from argparse import ArgumentParser

url = environ.get('FTDI_DEVICE', 'ftdi:///1')

parser = ArgumentParser(prog='Planter', description='Waters plants')
parser.add_argument('duration', type=float)

args = parser.parse_args()

gpio = GpioAsyncController()
gpio.configure(url, direction=0xff)
port = gpio.get_gpio()

gpio.write(0xff)
sleep(args.duration)
gpio.write(0x00)