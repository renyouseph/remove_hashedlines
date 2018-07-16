### Requirements ###
# apt-get update
#apt-get install python3
###

import os

logfile = '/root/python/files/testfile.txt'
writefile = '/root/python/files/writefile.txt'

with open(logfile,'r') as fhRead:
    with open(writefile,'w') as fhWrite:
        for line in fhRead:
            line = line.rstrip('\n')
            if not line.startswith('#'):
                fhWrite.write(line)
                fhWrite.write('\n')
