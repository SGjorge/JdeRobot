#!/usr/bin/env python
import sys,traceback,Ice
import HW

iceObject = None

try:
	# create Ice object an proxy to server
	iceObject = Ice.initialize(sys.argv)
	proxy = iceObject.stringToProxy("SimplePrinter:default -p 10000")

	# create object who talks to server
	printer = HW.PrintPrx.checkedCast(proxy) # Be carefull PrintPrx will be creat when compile with slice2py
	if not printer:
		raise RuntimeError("Invalid proxy")

	# request to server
	printer.printString("Hello world in ICE")

except:
	traceback.print_exc()

if iceObject:
	try:
		iceObject.destroy()
	except:
		traceback.print_exc()

sys.exit(0)