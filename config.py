#!/usr/bin/env python
# Clash of Clans - IRC Stats Bot and Announcer
# coded by vorteckz@vorteckzstudios.online

class config:
    class clashconfig:
        tag = "#28R992YJR"
    class irc:
        server = 'localhost'
        port = 6697
        username = 'sod'
        realname = 'ClashIRCBot by vorteckz'
        nickname = 'SPeLLoFDeATH'
        channel = '#vorteckz'
        channelkey = ''
        password = None
        ssl = True
        v6 = 2
        vhost = None
        
    class throttle:
        cmd       = 1
        msg       = 0.5
        reconnect = 10
        rejoin    = 3
        last      = 0
        slow      = False
        lastnick  = None
        
        
