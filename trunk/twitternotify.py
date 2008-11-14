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

import twitter
from threading import Thread
from pythonutils import ConfigObj

class TwitterNotifyThread(Thread):
    
    def __init__(self, user, passwd, to, msg):
        Thread.__init__(self)
        self.user = user
        self.passwd = passwd
        self.to = to
        self.msg = msg
        
    def run(self):
        api = twitter.Api(username=self.user, password=self.passwd)
        api.PostDirectMessage(self.to, self.msg)
        

class TwitterNotify:
    def __init__(self, user, password):
        self.user = user
        self.passwd = password
        
    def __init__(self, configFile):
        config = ConfigObj(configFile)
        self.user = config['user']
        self.passwd = config['password']
        
    def notify(self, to, msg):
        t = TwitterNotifyThread(self.user, self.passwd, to, msg)
        t.start()