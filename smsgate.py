#!/usr/bin/env python

import sys

import gobject

import dbus
import dbus.mainloop.glib

redir = sys.argv[1]

def got_sms(frm, timestamp, contents):
    print "got sms from %r\n%s\n=====" %(frm, contents)

    gsm_sms_iface.SendTextMessage(redir, "%s: %s" %(frm, contents), False )

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()

device = bus.get_object( 'org.freesmartphone.ogsmd', '/org/freesmartphone/GSM/Device' )
gsm_sms_iface = dbus.Interface(device, 'org.freesmartphone.GSM.SMS')

device.connect_to_signal("IncomingTextMessage", got_sms, dbus_interface="org.freesmartphone.GSM.SMS")

loop = gobject.MainLoop()
loop.run()
