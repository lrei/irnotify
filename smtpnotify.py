from smtplib import SMTP

fromaddr = "notification.bot@borg.fe.up.pt"
toaddr = "luis.rei@gmail.com"
sub = "NANANANA"
msg = 'Hello Rei'
server = SMTP('localhost')
server.sendmail(fromaddr, toaddr, sub, msg)
server.quit()