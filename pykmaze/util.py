#-----------------------------------------------------------------------------
# Communicate w/ a Decathlon Keymaze 500/700 devices
#-----------------------------------------------------------------------------
# @author Emmanuel Blot <manu.blot@gmail.com> (c) 2009
# @license MIT License, see LICENSE file
#-----------------------------------------------------------------------------

import time

def hexdump(data):
    """Convert a binary buffer into a hexadecimal representation."""
    LOGFILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
    src = ''.join([chr(x) for x in data])  # Aquesta línia converteix la llista de bytes a string
    length = 16
    result = []
    for i in range(0, len(src), length):  # 'xrange' es canvia per 'range' en Python 3
        s = src[i:i+length]
        hexa = ' '.join(["%02x" % ord(x) for x in s])
        printable = s.translate(str.maketrans(LOGFILTER))
        result.append("%06x   %-*s   %s\n" % (i, length*3, hexa, printable))
    return ''.join(result)

def inttime(dt):
    return int(time.mktime(dt.timetuple()))
