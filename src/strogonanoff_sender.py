#!/usr/bin/env python

from time import time
from strogonanoff_common import *

def print_bitstream(state_list):
    val = []
    for state in state_list: val.append(str(state))
    print "data:", ''.join(val)

def print_send_info(pin_number, pulse_width, state_list):
    print "send to pin:", pin_number.gpio_number, \
          "pulse width:", pulse_width/1e-6, "us"
    print_bitstream(state_list)

def busy_wait_until(end_time):
    while time() <= end_time: pass

def send_bitstream(pin_number, state_list, verbose, pulse_width):
    if verbose: print_send_info(pin_number, pulse_width, state_list)
    end_time = time()
    for state in state_list:
        end_time = end_time + pulse_width
        pin_number.set_value(state)
        busy_wait_until(end_time)

def encode_bitstream(channel, button, on):
    result = []
    for i in range(6):
        result.extend(BIT_CODE[channel-1] + BIT_CODE[button-1] + UNKNOWN_CODE)
        result.extend(ON_CODE if on else OFF_CODE)
        result.extend(SYNC)
    return result

def send_command(pin, channel, button, on, verbose, pulse_width=DEFAULT_PULSE_WIDTH):
    send_bitstream(pin, encode_bitstream(channel, button, on), verbose, pulse_width)

def main():
    from WiringPin import WiringPin
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-b", "--button", type="int", default=1)
    parser.add_option("-c", "--channel", type="int", default=1)
    parser.add_option("-g", "--gpio", type="int", default=0)
    parser.add_option("-v", "--verbose", action="store_true", default=False)
    (options, args) = parser.parse_args()
    on = True if len(args) == 0 or args[0] != "off" else False
    pin = WiringPin(options.gpio).export()
    send_command(pin, options.channel, options.button, on, options.verbose)
 
if __name__ == "__main__":
    main()
