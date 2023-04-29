#!/usr/bin/python3
for alphabets in range(97,123):
    if chr(alphabets) in ['q','e']:
        continue
    else:
        print(chr(alphabets),end="")
