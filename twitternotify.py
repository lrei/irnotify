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