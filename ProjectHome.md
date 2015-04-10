Currently mostly proof of concept code. Mail isn't working yet.

Uses xmpppy and python-twitter.

## Examples: ##
### Twitter DM ###
```
from twitternotify import TwitterNotify
n = TwitterNotify("twitter.conf")
n.notify("lrei", "How do you feel, Rei?")
```
### XMPP message ###
```
from xmppnotify import XMPPNotify
n = XMPPNotify("xmpp.conf")
n.notify("luis.rei@gmail.com", "How do you feel, Rei?")
```