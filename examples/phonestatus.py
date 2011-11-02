#!/usr/bin/env python
import plivocldhelper
import sys

try:
    phone = sys.argv[1]
except:
    print "Need Phone"
    sys.exit(1)

# Sid and AuthToken
SID = 'MTFMMJMZNTRHYTEXMTVM'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {
    'Phone' : phone
}

try:
    result = plivo.phone_status(params)
    print result
except Exception, e:
    print e
    raise


