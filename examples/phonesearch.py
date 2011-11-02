#!/usr/bin/env python
import plivocldhelper
import sys

try:
    npa = sys.argv[1]
except:
    print "Need AreaCode"
    sys.exit(1)
try:
    nxx = sys.argv[2]
except:
    nxx = ""

# Sid and AuthToken
SID = 'MTFMMJMZNTRHYTEXMTVM'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {
    'AreaCode' : npa,
    'ExchangeCode' : nxx,
    'Quantity' : 5,
}

try:
    result = plivo.phone_search(params)
    print result
except Exception, e:
    print e
    raise


