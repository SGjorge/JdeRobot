# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `hw.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module HW
_M_HW = Ice.openModule('HW')
__name__ = 'HW'

if 'Print' not in _M_HW.__dict__:
    _M_HW.Print = Ice.createTempClass()
    class Print(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_HW.Print:
                raise RuntimeError('HW.Print is an abstract class')

        def ice_ids(self, current=None):
            return ('::HW::Print', '::Ice::Object')

        def ice_id(self, current=None):
            return '::HW::Print'

        def ice_staticId():
            return '::HW::Print'
        ice_staticId = staticmethod(ice_staticId)

        def printString(self, str, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_HW._t_Print)

        __repr__ = __str__

    _M_HW.PrintPrx = Ice.createTempClass()
    class PrintPrx(Ice.ObjectPrx):

        def printString(self, str, _ctx=None):
            return _M_HW.Print._op_printString.invoke(self, ((str, ), _ctx))

        def begin_printString(self, str, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_HW.Print._op_printString.begin(self, ((str, ), _response, _ex, _sent, _ctx))

        def end_printString(self, _r):
            return _M_HW.Print._op_printString.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_HW.PrintPrx.ice_checkedCast(proxy, '::HW::Print', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_HW.PrintPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_HW._t_PrintPrx = IcePy.defineProxy('::HW::Print', PrintPrx)

    _M_HW._t_Print = IcePy.defineClass('::HW::Print', Print, -1, (), True, False, None, (), ())
    Print._ice_type = _M_HW._t_Print

    Print._op_printString = IcePy.Operation('printString', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_HW.Print = Print
    del Print

    _M_HW.PrintPrx = PrintPrx
    del PrintPrx

# End of module HW
