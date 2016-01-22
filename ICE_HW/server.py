#!/usr/bin/env python
import sys,traceback,Ice
import HW

""" class extends to HW dir, to have HW shuold be compile hw.ice with slice2py"""
class PrintHw(HW.Print):
	def printString(self,s,current=None):
		print s

iceObject = None
try:
	""" create object to connect with us"""
	iceObject = Ice.initialize(sys.argv)
	adapter = iceObject.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000") #iceObject is tied to End Point
	object = PrintHw() # creat an object to class PrintHW

	""" iceObject is launched and it wait for a connection """
	adapter.add(object, iceObject.stringToIdentity("SimplePrinter")) #creat the socket
	adapter.activate() #lauch the connection
	iceObject.waitForShutdown() 

except:
	traceback.print_exc()
	sys.exit(1)

if iceObject:
	try:
		iceObject.destroy()
	except:
		traceback.print_exc()
		sys.exit(1)

sys.exit(0)