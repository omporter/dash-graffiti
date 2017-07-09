#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.graffiti import *

string = "Thanks Evan Duffield"

print('Write graffiti "' + string + '" to blockchain by sending some duffs to:\n')
print(generate_graffiti_address(string))
