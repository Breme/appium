'''
Created on Aug 9, 2018

@author: sysadmin
'''
for attempt in range(3):
    try:
# do thing
        print "yees"
    except:
        print 'bi'
# perhaps reconnect, etc.
    else:
        break
else:
    print 'hey'