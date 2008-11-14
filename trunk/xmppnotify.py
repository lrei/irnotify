# Copyright (c) 2008 Luis Rei <luis.rei@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import xmpp, time
from threading import Thread
from pythonutils import ConfigObj

class XMPPNotifyThread(Thread):
    
    def __init__(self, user, passwd, tojid, msg):
        Thread.__init__(self)
        self.status = 0
        self.user = user
        self.passwd = passwd
        self.tojid = tojid
        self.msg = msg
        
    def run(self):
        jid = xmpp.protocol.JID(self.user)
        cl = xmpp.Client(jid.getDomain(),debug=[])

        con = cl.connect()
        if not con:
            self.status = 1
        
        auth = cl.auth(jid.getNode(), self.passwd, resource=jid.getResource())
        if not auth:
            self.status = 2

        cl.send(xmpp.protocol.Message(self.tojid, self.msg))
        time.sleep(10)

class XMPPNotify:
    def __init__(self, user, password):
        self.user = user
        self.passwd = password
        
    def __init__(self, configFile):
        config = ConfigObj(configFile)
        self.user = config['user']
        self.passwd = config['password']
        
    def notify(self, tojid, msg):
        t = XMPPNotifyThread(self.user, self.passwd, tojid, msg)
        t.start()
