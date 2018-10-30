#!/usr/bin/python

import sys

PATH="/usr/local/lib/python2.6/site-packages"
sys.path.append(PATH)
import pexpect, traceback

user='username'
host='hostname'
passwd="passpasswd"

ssh_newkey = 'Are you sure you want to continue connecting'
# my ssh command line
ssh_cmd="ssh %s -l %s" %(host,user)
p=pexpect.spawn(ssh_cmd)
i=p.expect([ssh_newkey,'assword:','[#\$\%\]\>] ', pexpect.EOF],timeout=120)
if i==0:
        #match ssh_newkey 
        print "send yes"
        p.sendline('yes')
        i=p.expect([ssh_newkey,'assword:','[#\$\%\]\>] ', pexpect.EOF],timeout=120)
       i=p.expect([ssh_newkey,'assword:','[#\$\%\]\>] ', pexpect.EOF],timeout=120)
if i==1:
        #match passwd 
        print "send password"
        p.sendline(passwd)
        i = p.expect (['Permission denied', 'Terminal type', '[#\$\%] ','assword:'],timeout=120)
        if i==0:
            #match Permission denied 
            print 'Permission denied on host. Can\'t login'
            p.kill(0)
        elif i==1:
            print 'Login OK... need to send terminal type.'
            p.sendline('vt100')
            p.expect ('[#\$\%] ')
        elif i==2:
            print 'Login OK.'
            print 'Shell command prompt', p.after
        elif i==3:
            p.sendline(passwd)
elif i==2:
        print "passwd alread set? public key provided?\n"
        pass
elif i==3:
        print "either got no key or connection timeout"
        pass
print p.before # print out the result
p.sendline('source .cshrc.cz')
p.expect ('[#\$\%] ')
p.sendline('bash')
p.expect ('[#\$\%] ')
p.interact()
