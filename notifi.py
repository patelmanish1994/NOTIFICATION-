#!/usr/bin/env python

import pynotify

def sendmessage(title, message):
    pynotify.init("notify")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
title="hello manish"
message="this is the notification"
sendmessage(title, message)



