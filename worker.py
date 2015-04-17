#!/usr/bin/python

from Printer.Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

printer.wake()
printer.flush()
printer.setDefault()

printer.setLineHeight(20)
printer.justify('C')
printer.setSize('L')
printer.inverseOn()

printer.println('@nearengine')

printer.inverseOff()
printer.setSize('M')

printer.println('researchaz.org #141')

printer.setLineHeight()
printer.setSize('S')

printer.println('Wed, 18 Feb 2015 11:16 pm MST')

printer.feed(1)
printer.justify('L')

printer.println('Show Preview doesn\'t work without edit to body for existing blog post')

printer.setLineHeight(40)

printer.println('*** BUG')
printer.println('*** HIGH PRIORITY')
printer.println('*** MEDIUM COMPLEXITY')

printer.setLineHeight()
printer.feed(3)

printer.setDefault()
printer.flush()
printer.sleep()
