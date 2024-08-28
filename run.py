from os import environ
from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioAsyncController
from time import sleep
from argparse import ArgumentParser
from datetime import datetime, timedelta

url = environ.get('FTDI_DEVICE', 'ftdi:///1')

parser = ArgumentParser(prog='Planter', description='Waters plants')
parser.add_argument('duration', type=float)

args = parser.parse_args()

print("Running planter for {0} seconds".format(args.duration))

def debug_print(message):
    print("{0} {1}".format(datetime.now().isoformat(), message))

# DBUS
gpio = GpioAsyncController()
gpio.configure(url, direction=0xff)
# port = gpio.get_gpio()

# CBUS
# To use CBUS the Pin mode *must* be set in the EEPROM to I/O Mode
# Use FT_PROG/ftconf to write to EEPROM:
#  https://ftdichip.com/utilities/#ft_prog
#  https://eblot.github.io/pyftdi/eeprom.html#ftconf
ftdi = Ftdi.create_from_url(url)
ftdi.set_cbus_direction(0x0f, 0x0f)

def set_pins(level = "low"):
    if level == "high":
        gpio.write(0xff)            # DBUS
        ftdi.set_cbus_gpio(0x0f)    # CBUS
    else:
        gpio.write(0x00)            # DBUS
        ftdi.set_cbus_gpio(0x00)    # CBUS

debug_print("Connected")

start_time = datetime.now()
stop_time = start_time + timedelta(seconds=args.duration)

set_pins("high")
debug_print("on")

while datetime.now() < stop_time:
    sleep(1)

set_pins("low")
debug_print("off")

debug_print("Done")