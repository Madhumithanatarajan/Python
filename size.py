import os
statinfo = os.stat('addition.py')
statinfo
print(statinfo.st_size)
