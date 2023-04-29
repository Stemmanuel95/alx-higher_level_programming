#!/usr/bin/env python3
for alphabet in range(ord('a'), ord('z')+1):
    if alphabet == ord('q') or alphabet == ord('e'):
        continue
    print("{}".format(chr(alphabet)), end="")
