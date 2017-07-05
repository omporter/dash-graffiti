#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.b58 import *
from lib.hashs import *

long = int
_bchr = lambda x: bytes([x])

data = "Thanks Evan Duffield"

length = len(data)
print("Data lenght: " + str(length))
if length > 20:
   print("ERROR: Input string is too long")
   print("Insert 20 characters or less")
   exit()

for x in range(length, 20):
   data = data + "\x00"

data_as_byte = str.encode(data)

addr_prefix = 76  # 4c
addr_prefix_as_byte = _bchr(addr_prefix)

vs = addr_prefix_as_byte + data_as_byte
# print(vs)
# vshex = binascii.hexlify(data_as_byte)
# print(vshex)

check = double_sha256(vs)[0:4]

encpay = vs + check

base58_encpay = b58encode(encpay)
print('Write graffiti "' + data + '" to blockchain by sending some duffs to:\n')
print(base58_encpay)
