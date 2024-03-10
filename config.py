#!/usr/bin/env python
# Clash of Clans - IRC Stats Bot and Announcer
# coded by vorteckz@vorteckzstudios.online

class config:
    class clashconfig:
        tag = "#28R992YJR" # clan tag
    class irc:
        server = 'irc.supernets.org'
        port = 6697
        username = 'sod'
        realname = 'ClashIRCBot by vorteckz'
        nickname = 'SPeLLoFDeATH'
        channel = '#vorteckz'
        adminpassword = 'loginpassword'
        channelkey = ''
        password = None
        ssl = True # only turn on if your IRC server port supports ssl
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
        
        

