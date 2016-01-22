#!/usr/bin/env python
import sys,traceback,Ice
import HW

class PrintHw(HW.Print):
	def printString(self,s,current=None):
		print s

iceObject = None
try:
	iceObject = Ice.initialize(sys.argv)
	adapter = iceObject.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
	object = PrintHw()

	adapter.add(object, iceObject.stringToIdentity("SimplePrinter"))
	adapter.activate()
	iceObject.waitForShutdown()

except:
	traceback.print_exc()

if iceObject:
	try:
		iceObject.destroy()
	except:
		traceback.print_exc()

sys.exit(0)