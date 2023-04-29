#!/usr/bin/env python3

for alphabet in range(97, 123):
    if chr(alphabet) in ['q', 'e']:
        continue
    else:
        print(chr(alphabet), end="")
